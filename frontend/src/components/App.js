import React from "react";
import ReactDOM from "react-dom";
import DataFetcher from "./DataFetcher";
import TableDisplay from "./TableDisplay";
const App = () => (
  <DataFetcher endpoint="api/coindesk/"
                render={data => <TableDisplay data={[data]} />} />
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
