# Vuex
1. status : 데이터 저장소
2. getters : = computed 바로 계산되는 곳
3. mutations & actions : 함수가 저장되는 곳

## state
- $store.state 로 접근 가능
- 해당 state가 변화하면 공유하는 component들이 전부 갱신됨
## mutations
- state 자체를 변경하는 유일한 방법
- mutation, action안에 있는 함수는 핸들러 함수라 불린다
- 그리고 해당 함수들은 분명히 동기적인 함수들만 작성 (변화의 시점을 알 수 있다)
- 첫번째 인자를 state로 받는다
- component에서 commit()메서드로 호출됨
## actions
- 위의 mutation과 유사하지만, 비동기 작업이 포함될 수 있다
- 따라서 state를 직접 변경 하지 않음
- context를 통해 다른 모든 요소를 접근 가능
- dispatch()의 메서드로 호출
- action은 backend api와 통신을 담당하게 된다
## getters
- computed역할
- state변화 시키지 않고 계산시 활용
- getters값은 cache된다
- 종속 값이 변화 시 재계산됨
- 첫번째 인자는 state, 두번째 인자는 getter

# app.vue에서의 actions과 mutations
```javascript
// 위에서 v-model로 inputData묶어둠
computed : {
  message () {
    return this.$store.state.message
  },
  messagelength() {
    return this.$store.getters.messageLength // 함수 이름으로 호출하자
  }
}
methods: {
  changeMessage() {
    const newMessage = this.inputData
    this.$store.dispatch ('액션 메서드 이름', newMessage(추가 데이터, payload)    )
  }
}
```
```javascript
// index.js
export default new Vuex.Store({
  getters : {
    messageLength(state) {
      return state.message.length
    }
  }
  mutations : {
    CHANGE_MESSAGE(state, newMessage){
      // mutation은 state를 직접적으로 변경하기 위함
      state.message = newMessage
    }
  }
  actions :{
    changeMessage(context, newMessage) {
      context.commit('mutations 메서드 이름', 추가데이터)
    }
  }
})
```

# lifecycle hooks
- vue의 인스턴스는 생성과 소멸의 단계별 초기화 과정을 거치게 된다
- 단계가 트리거가 되어 로직 수행 가능
- 해당 함수들은 export default안의, method밖에 작성해주면 된다
- 트리거들이 작동하면서 함수들이 차례로 작동하게 되는 방법이다

## triggers
- 참고로 해당 trigger들과의 이름이 동일해야만 작동하게 됩니다 !!!!!
- instance 마다 각각의 lifecycle을 가지고 있음
- component 마다 각각이 되어 있다. 즉, 따로 작성해주고, 따로 동작하게 되는 것
### created
- vue instance 가 생성 직후 호출 됨
- data, computed설정이후
- 다만, mount 되기 전의 상황이다
- 따라서 dom에는 접근 불가능 
### mounted
- mount 된 직후 호출됨
- mount된 요소 변경 가능
### updated
- 데이터가 변경되어 dom에 변화를 줄때 작동
- 처음 created 되면서도 변화를 줬으면 작동하는 듯
- 

# Todos
- 만약 작성하는 과정에서 null값을 방지하고 싶거나 공백을 제거하고 싶은 경우
- 처음에 받아오는 vue에서 이러한 부분이 동작하지 않도록 방지하는것이 효율적

# vuex
- 결국 어플의 크기가 커지거나 관리하기 어려운 순간이 올 경우에 자연스럽게 선택하도록 하자