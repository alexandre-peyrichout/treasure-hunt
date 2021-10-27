import { useState, useEffect } from "react";

const Input = ({ notifyParent }) => {
  const [value, setValue] = useState("1");
  const handleChange = (e) => {
    setValue(e.target.value);
    notifyParent(value);
  };

  return (
    <input
      type="number"
      min={1}
      max={9}
      value={value}
      onChange={handleChange}
    ></input>
  );
};

export default Input;
