import React from "react";
// import StockWidget from "./components/StockWidget";

export default class App extends React.PureComponent {
  render() {
    return (
      <div className="h-screen flex justify-center items-center">
        {/* <StockWidget symbols={[["SBIN"], ["SBICARD"], ["SBILIFE"]]} /> */}
        <div className="text-2xl">ESNSE</div>
      </div>
    );
  }
}
