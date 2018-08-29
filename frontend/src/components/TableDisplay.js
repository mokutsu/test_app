import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const TableDisplay = ({ data }) =>
  !data ? (
    <p>Nothing to show</p>
  ) : ( {data});
TableDisplay.propTypes = {
  data: PropTypes.array.isRequired
};
export default TableDisplay;
