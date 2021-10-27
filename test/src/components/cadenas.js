import { useState, useMemo } from "react";
import Input from "./input";

const Cadenas = () => {
  const [finalCode, setFinalCode] = useState([]);
  const notifyParent = (value, index) => {
    setFinalCode((code) => {
      code[index] = value;
      return [...code];
    });
  };

  const displayedFinalCode = useMemo(() => {
    return finalCode.join("");
  }, [finalCode]);

  return (
    <div>
      <h1>{displayedFinalCode}</h1>
      <Input notifyParent={(value) => notifyParent(value, 0)} />
      <Input notifyParent={(value) => notifyParent(value, 1)} />
      <Input notifyParent={(value) => notifyParent(value, 2)} />
      <Input notifyParent={(value) => notifyParent(value, 3)} />
    </div>
  );
};

export default Cadenas;
