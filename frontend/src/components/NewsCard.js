import React from "react";

function NewsCard() {
  let data = {
    title:
      "SBI offers realty gold loan scheme for financing your dream house: Know features, interest rates and more",
    date: "11/11/21",
    gist: "The SBI has informed its customers about the Realty Gold Loan Scheme to get loan quickly and without any hassles. Get more Personal Finance...",
    link: "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=newssearch&cd=&ved=2ahUKEwjq87OGvI_0AhVQZt4KHfg5CmEQxfQBKAB6BAgVEAI&url=https%3A%2F%2Fwww.zeebiz.com%2Fpersonal-finance%2Fnews-sbi-offers-realty-gold-loan-scheme-for-financing-your-dream-house-know-features-interest-rates-and-more-170327&usg=AOvVaw1Bu4ln8TPLIzpEdIK7mWJ1",
  };
  return (
    <div className="p-5 border-2 rounded-lg cursor-pointer shadow-md">
      <a href={data.link} className="space-y-2">
        <div className="text-lg">{data.title}</div>
        <div className="text-base">{data.gist}</div>
        <div className="text-sm">{data.date}</div>
      </a>
    </div>
  );
}

export default NewsCard;
