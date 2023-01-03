<template>
  <div>
    <h1 class="border">Welcome To My World</h1>
    <MyChild 
    static-props = "component down" 
    :my-props="dynamicProps"
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import MyChild from '@/components/MyChild';

export default {
  name: 'MyComponent',
  components:{
    MyChild,
  },
  data : function () {
    return {
      dynamicProps : "It's in data"
    }
  },
  methods:{
    parentGetEvent: function(inputdata){
      // console.log("발생 이벤트")
      console.log(`child send ${inputdata}`)
    },
    getDynamicData: function(inputdata) {
      console.log(`child send ${inputdata}`)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>