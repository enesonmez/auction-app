import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { useUser } from "../context/UserContext";
import axios from "axios";
import React, { useEffect, useState } from "react";

function NavBar() {
  const { user, isAuth, getUserInfo, setIsLogin, isLogin } = useUser();
  const logoutUrl = "http://localhost:5000/api/v1/auth/logout";

  useEffect(() => {
  }, []);

  async function logout() {
    await axios
      .get(logoutUrl, {
        withCredentials: true,
      })
      .then((data) => console.log(data))
      .then(() => {
        isAuth().then((value) => setIsLogin(value));
      })
      .catch((e) => console.log(e));
  }
  function sessionRemove() {
    logout();
  }
  return (
    <>
      <Navbar sticky="top" bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/">Auction App</Navbar.Brand>
          <Nav>
            {!isLogin ? (
              <Nav className="justify-content-end">
                <Nav.Link href="signup">Sign Up</Nav.Link>
                <Nav.Link href="login">Sign In</Nav.Link>
              </Nav>
            ) : (
              <Nav>
                <Nav.Link onClick={sessionRemove} href="login">
                  Sign Out
                </Nav.Link>
                <Nav>
                  <p
                    className="text-white"
                    style={{ margin: 0, paddingTop: 8, paddingLeft: 5 }}
                  >
                    {user.firstname} {user.lastname}
                  </p>
                </Nav>
              </Nav>
            )}
          </Nav>
        </Container>
      </Navbar>

      <br />
    </>
  );
}

export default NavBar;
