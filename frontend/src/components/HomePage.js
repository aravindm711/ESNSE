import React from "react";
import SearchBar from "./SearchBar";

function HomePage(props) {
  return (
    <div className="h-screen flex justify-center items-center">
      <div className="flex flex-col items-center">
        <p className="text-3xl p-2">ESNSE</p>
        <SearchBar setResult={props.setResult} />
      </div>
    </div>
  );
}

export default HomePage;
