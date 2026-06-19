import { useRef } from "react";
import "./App.css";

function App() {
  const nameRef = useRef<HTMLInputElement>(null);
  const emailRef = useRef<HTMLInputElement>(null);

  const goToEmail = () => {
    emailRef.current?.focus();
  };

  const clearFields = () => {
    if (nameRef.current) nameRef.current.value = "";
    if (emailRef.current) emailRef.current.value = "";
    nameRef.current?.focus();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>User Form</h2>

      <input ref={nameRef} placeholder="Name" />
      <br /><br />

      <input ref={emailRef} placeholder="Email" />
      <br /><br />

      <button onClick={goToEmail}>Go to Email</button>
      <button onClick={clearFields}>Clear All</button>
    </div>
  );
}

export default App;
