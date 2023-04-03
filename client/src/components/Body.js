import React, { useEffect, useState } from "react";
import { useUser } from "../context/UserContext";
import { init, send, subscribeOffer } from "../Socket/SocketApi";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Body() {
  const { user, isAuth, setIsLogin } = useUser();
  const productUrl = "http://localhost:5000/api/v1/product";
  const [items, setItems] = useState([{}]);
  const navigate = useNavigate();

  const onChangeHandler = (e) => {
    send({
      user_id: user.id,
      product_id: items[e.target.name].id,
      price: items[e.target.name].price + 5,
    });
  };

  useEffect(() => {
    isAuth().then((value) => setIsLogin(value))
    getAllProduct();
    init();
    subscribeOffer((items) => {
      setItems(items);
    });
  }, []);

  const getAllProduct = async () => {
    const _ = await axios
      .get(productUrl, { withCredentials: true })
      .then((resp) => {
        setItems(resp.data.data);
        console.log(resp)
      })
      .catch((e) => {
        if (e.response.status === 401) {
          navigate("/login");
          console.log(e.response);
        }
      });
  };

  return (
    <div>
      <div className="App">
        <ul>
          {items.map((item, i) => (
            <li key={i}>
              <div className="card">
                <img src={item.image_url} width="250" height="250" />
                <h4>{item.name}</h4>
                <p>Last Offer</p>
                <p>{item.email}</p>
                <p className="price">₺{item.price}</p>

                <button name={i} onClick={onChangeHandler}>
                  Increase the price
                </button>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Body;
