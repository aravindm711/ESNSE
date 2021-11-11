import React from "react";

function NewsCard({ data }) {
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
