<template>
  <div>
    <todolistitems
      v-for='(todo,index) in todos' :key="index"
      :todo="todo"
    />
    <!-- {{ todos }} -->
  </div>
</template>

<script>
import todolistitems from './todolistitems.vue';
export default {
  name: 'TodoList',
  components : {
    todolistitems
  },
  computed :{
    todos() {
      return this.$store.state.todos
    },
  },

}
</script>

<style>

</style>