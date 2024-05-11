import axios from "axios";

export default axios.create({
  baseURL: "https://blog-backend.dashgin.com/api/v1",
  responseType: "json"
});
