import axios from "axios";

export default axios.create({
  baseURL: "https://dashgin.herokuapp.com/api/v1",
  responseType: "json"
});
