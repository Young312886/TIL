<template>
  <div>
    <span @click="updateTodostat" 
     :class="{'completed' : todo.isCompleted}">{{ todo.title }}</span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name:'TodoListItems',
  props: {
    todo: Object,
  },
  methods : {
    deleteTodo() {
      this.$store.dispatch('deleteTodo', this.todo)
      // this.$store.commit('DELETE_TODO',this.todo)
    },
    updateTodostat() {
      this.$store.dispatch('updatestat', this.todo)
    }
  }
}
</script>

<style>
.completed {
  text-decoration: line-through;
}
</style>