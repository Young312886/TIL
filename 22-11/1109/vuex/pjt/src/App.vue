<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2> {{ todoscount }} </h2>
    <h2>{{ completed }}</h2>
    <todoList/>
    <todoform/>
    <!-- <button @click="load">불러오기</button> -->
  </div>
</template>

<script>
import todoform from './components/todoform.vue';
import todoList from './components/todoList.vue';
export default {
  name: 'App',
  components: {
    todoList,
    todoform
  },
  computed: {
    todoscount (){
      return this.$store.getters.alltodocount
    },
    completed(){
      return this.$store.getters.completed
    }

  },
  methods:{
    load(){
      this.$store.dispatch('load')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
