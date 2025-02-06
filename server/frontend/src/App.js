import LoginPanel from "./components/Login/Login";
import { Routes, Route, BrowserRouter, Navigate } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="*" element={<Navigate to="/login" />} />{" "}
      {/* Redirect unknown routes */}
    </Routes>
  );
}
export default App;
