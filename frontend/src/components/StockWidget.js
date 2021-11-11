import React from "react";

export default class StockWidget extends React.PureComponent {
  constructor(props) {
    super(props);
    this._ref = React.createRef();
  }
  componentDidMount() {
    var symbols = JSON.stringify(this.props.symbols);
    const scripttv = document.createElement("script");
    scripttv.src = "https://s3.tradingview.com/tv.js";
    scripttv.async = true;
    this._ref.current.appendChild(scripttv);
    const script = document.createElement("script");
    script.innerHTML = ` new TradingView.MediumWidget(
  {
  "symbols": ${symbols},
  "chartOnly": false,
  "width": 500,
  "height": 400,
  "locale": "in",
  "colorTheme": "transparent",
  "gridLineColor": "rgba(240, 243, 250, 0)",
  "fontColor": "#787B86",
  "isTransparent": false,
  "autosize": false,
  "showFloatingTooltip": true,
  "showVolume": false,
  "scalePosition": "no",
  "scaleMode": "Normal",
  "fontFamily": "Trebuchet MS, sans-serif",
  "noTimeScale": false,
  "chartType": "area",
  "lineColor": "#2962FF",
  "bottomColor": "rgba(41, 98, 255, 0)",
  "topColor": "rgba(41, 98, 255, 0.3)",
  "container_id": "tradingview_15cf2"
}
  );`;
    this._ref.current.appendChild(script);
  }
  render() {
    return (
      <div
        className="border-2 rounded-lg shadow-md tradingview-widget-container"
        ref={this._ref}
      >
        <div id="tradingview_15cf2"></div>
      </div>
    );
  }
}
