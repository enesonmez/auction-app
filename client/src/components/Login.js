import axios from "axios";
import { useFormik } from "formik";
import React from "react";
import { Button, Form, InputGroup } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { useUser } from "../context/UserContext";
import { LoginValidations } from "./Validations";

function Login() {
  const loginUrl = "http://localhost:5000/api/v1/auth/login";
  const { user, isAuth, getUserInfo, setIsLogin, isLogin } = useUser();
  const navigate = useNavigate();
  const { handleSubmit, handleChange, values, errors, touched, handleBlur } =
    useFormik({
      initialValues: {
        email: "",
        password: "",
      },
      onSubmit: async (values) => {
        await axios
          .post(loginUrl, values, {
            withCredentials: true,
            headers: {
              "Content-Type": "application/json",
            },
          })
          .then((res) => console.log(res.data))
          .then(()=>{
            isAuth().then((value) => setIsLogin(value))
          })
          .then(() => {
            navigate("/");
          })
          .catch((e) => {
            console.log(e.response.data.messsage);
          });
      },
      validationSchema: LoginValidations,
    });
  return (
    <div className="App">
      <form onSubmit={handleSubmit} className="form-padding">
        <InputGroup className="mb-3">
          <InputGroup.Text id="basic-addon1">Email</InputGroup.Text>
          <Form.Control
            name="email"
            onChange={handleChange}
            onBlur={handleBlur}
            value={values.email}
            placeholder="Mail"
            aria-label="Mail"
            aria-describedby="basic-addon1"
          />
        </InputGroup>
        {errors.email && touched.email && (
          <div className="error">{errors.email}</div>
        )}
        <InputGroup className="mb-3">
          <InputGroup.Text id="basic-addon1">Password</InputGroup.Text>
          <Form.Control
            type="password"
            name="password"
            onChange={handleChange}
            onBlur={handleBlur}
            value={values.password}
            placeholder="Password"
            aria-label="Password"
            aria-describedby="basic-addon1"
          />
        </InputGroup>
        {errors.password && touched.password && (
          <div className="error">{errors.password}</div>
        )}
        <br />
        <Button as="input" variant="dark" type="submit" value="Sign In" />
      </form>
    </div>
  );
}

export default Login;
