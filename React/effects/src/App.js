import { useState, useEffect } from "react";

function App() {
  const [keyword, setKeyword] = useState("");
  const [counter, setValue] = useState(0);
  const onClick = () => setValue((prev) => prev + 1);
  console.log("all the time");
  const once = () => {
    console.log("once");
  };
  // useEffect를 활용하면 전체 render 가운데에 해당 함수는 한번만 실행되게 된다
  // 따라서 값을 절대 고정 시킬 수 있다
  const onChange = (event) => setKeyword(event.target.value);

  useEffect(once, []);
  useEffect(() => {
    if (keyword !== "" && keyword.length > 5) {
    console.log("Call api");}
  }, [keyword]);
  // 위의 keyword가 변화하면 해당 effect가 동작하게 된다
  return (
    <div>
      <input
        value={keyword}
        onChange={onChange}
        type="text"
        placeholder="Search hear.."
      />
      <h1>{counter}</h1>
      <button onClick={onClick}> click me </button>
    </div>
  );
}

export default App;
