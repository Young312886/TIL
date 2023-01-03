<template>
  <div>
    <h3>This is child</h3>
    <p>{{ staticProps }}</p>
    <p>{{ myProps }}</p>
    <input type="text"
    v-model="childInputData"
    @keyup.enter = "childInput">
    <button @click="ChildToParent">클릭</button><br>

  </div>
</template>

<script>
export default {
  name : 'MyChild',
  props : {
    staticProps: String,
    myProps : String,
  },
  data:function(){
    return {
      childInputData:null,
    }
  },
  methods: {
    ChildToParent : function(){
      this.$emit('child-to-parent','child data')
    },
    childInput : function(){
      this.$emit('child-input', this.childInputData)
      this.childInputData= ''
    }
  }
}
</script>

<style>

</style>