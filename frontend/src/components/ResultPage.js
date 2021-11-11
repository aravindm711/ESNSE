import React from "react";
import SearchBar from "./SearchBar";
import NewsCard from "./NewsCard";
import StockWidget from "./StockWidget";

function ResultPage(props) {
  return (
    <div className="p-5">
      <div className="p-5 flex space-x-5 items-center">
        <div className="text-xl cursor-pointer">ESNSE</div>
        <div className="w-1/2">
          <SearchBar />
        </div>
      </div>
      <div className="flex space-x-5 p-4">
        <div className="w-2/3 space-y-5">
          <NewsCard />
          <NewsCard />
          <NewsCard />
          <NewsCard />
        </div>
        <div>
          <StockWidget symbols={[["SBIN"], ["SBICARD"], ["SBILIFE"]]} />
        </div>
      </div>
    </div>
  );
}

export default ResultPage;
