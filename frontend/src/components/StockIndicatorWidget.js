import React from "react";

export default class StockIndicatorWidget extends React.PureComponent {
  constructor(props) {
    super(props);
    this._ref = React.createRef();
  }
  componentDidMount() {
    const symbol = JSON.stringify(`NSE:${this.props.symbol}`);
    const script = document.createElement("script");
    script.src =
      "https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js";
    script.async = true;
    script.innerHTML = `{
  "interval": "1M",
  "width": 425,
  "isTransparent": true,
  "height": 450,
  "symbol": ${symbol},
  "showIntervalTabs": true,
  "locale": "in",
  "colorTheme": "light"
}`;
    this._ref.current.appendChild(script);
  }
  render() {
    return (
      <div
        className="border-2 rounded-lg shadow-md tradingview-widget-container"
        ref={this._ref}
      >
        <div className="tradingview-widget-container__widget"></div>
      </div>
    );
  }
}
