import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from "./PageComponents/HomePage/Home"
import Cart from "./PageComponents/CartPage/Cart"
import Profile from "./PageComponents/ProfilePage/Profile"
import Configuration from "./PageComponents/ConfigurationPage/Configuration"
import Reservation from "./PageComponents/ReservationPage/Reservation"
import Login from "./PageComponents/LoginPage/Login"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/configuration" element={<Configuration />} />
        <Route path="/reservation" element={<Reservation />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)