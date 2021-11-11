import React from "react";
import SearchBar from "./SearchBar";
import NewsCard from "./NewsCard";
import StockWidget from "./StockWidget";
import StockInfoWidget from "./StockInfoWidget";
import StockIndicatorWidget from "./StockIndicatorWidget";

function ResultPage({ result, setResult }) {
  let tickers = [];
  result.stocks.map((symbol) => tickers.push([symbol._source.SYMBOL]));
  return (
    <div className="p-5">
      <div className="p-5 flex space-x-5 items-center">
        <div onClick={() => setResult(null)} className="text-xl cursor-pointer">
          ESNSE
        </div>
        <div className="w-1/2">
          <SearchBar setResult={setResult} />
        </div>
      </div>
      <div className="flex space-x-5 p-4">
        <div className="w-4/6 space-y-5">
          <div className="h-96">
            <StockWidget symbols={tickers} />
          </div>
          {result.news.map((item) => (
            <NewsCard data={item._source} key={item._id} />
          ))}
        </div>
        <div className="felx flex-col space-y-5">
          <div className="h-96">
            <StockInfoWidget symbol={tickers[0][0]} />
          </div>
          <div className="h-96">
            <StockIndicatorWidget symbol={tickers[0][0]} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default ResultPage;
