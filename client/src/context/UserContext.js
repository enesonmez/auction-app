import { createContext, useContext, useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";

const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState({});
  const [isLogin, setIsLogin] = useState(false);
  const meUrl = "http://localhost:5000/api/v1/auth/me";

  useEffect(() => {}, [user]);

  useEffect(() => {}, [isLogin]);

  async function  isAuth() {
    let status = false
    const _ = await axios
      .get(meUrl, { withCredentials: true })
      .then((resp) => {
        setUser(resp.data.data);
        console.log(resp)
        status =  true
      })
      .catch((e) => {
        status = false
      });
    return status
  }


  const values = {
    user,
    setUser,
    isLogin,
    setIsLogin,
    isAuth,
  };

  return <UserContext.Provider value={values}>{children}</UserContext.Provider>;
};

export const useUser = () => useContext(UserContext);
