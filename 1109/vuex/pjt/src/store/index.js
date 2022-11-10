import Vue from 'vue'
import Vuex from 'vuex'
import createdPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins : [
    createdPersistedState(),
  ],
  state: {
    todos : [
      {
        title:'할일 1',
        isCompleted : false,
      },

    ]
  },
  getters: {
    alltodocount(state) {
      return state.todos.length
    },
    completecount(state) {
      return state.todos.filter((todo) => {
        return todo.isCompleted
      }).length
    },
    uncompleted (state, getters) {
      return getters.alltodocount - getters.completecount
    }
  },
  mutations: {
    CREATE_TODO (state, todo) {
      state.todos.push(todo)
    },
    DELETE_TODO (state, todo) {
      const index = state.todos.indexOf(todo)
      state.todos.splice(index,1)
    },
    UPDATETODOSTAT(state, todos) {
      state.todos.map((todo) => {
        if (todo === todos) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
    // LOAD(state) {
    //   const local = localStorage.getItem('save')
    //   const parsedlocal = JSON.parse(local)
    //   state.todos = parsedlocal
    // }
  },
  actions: {
    createTodo(context, todo) {
      const todoItem = {
        title: todo,
        isCompleted: false,
      }
      console.log(todoItem)
      context.commit('CREATE_TODO',todoItem)
      // context.dispatch('savetodos')
    },
    deleteTodo(context, todo) {
      context.commit('DELETE_TODO',todo)
      // context.dispatch('savetodos')
    },
    updateTodostat(context, todo) {
      context.commit('UPDATETODOSTAT', todo)
      // context.dispatch('savetodos')
    },
    // savetodos(context) {
    //   const jsontodos = JSON.stringify(context.state.todos)
    //   localStorage.setItem("save", jsontodos)
    // },
    // load(context) {
    //   context.commit('LOAD')
    // }
  },
  modules: {
  }
})
