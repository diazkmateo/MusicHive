import { Routes, Route } from 'react-router-dom';
import { AppProvider } from './context/AppContext';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import About from './pages/About';
import Profile from './pages/Profile';
import Albums from './pages/Albums';
import Songs from './pages/Songs';
import Artists from './pages/Artists';
import Genres from './pages/Genres';
import Collections from './pages/Collections';
import PrivateRoute from './components/PrivateRoute';
import './App.css';

function App() {
  return (
    <AppProvider>
      <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-grow">
        <Routes>
          <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
          <Route path="/about" element={<About />} />
            {/* Rutas protegidas */}
            <Route
              path="/profile"
              element={
                <PrivateRoute>
                  <Profile />
                </PrivateRoute>
              }
            />
            <Route
              path="/albums"
              element={
                <PrivateRoute>
                  <Albums />
                </PrivateRoute>
              }
            />
            <Route
              path="/songs"
              element={
                <PrivateRoute>
                  <Songs />
                </PrivateRoute>
              }
            />
            <Route
              path="/artists"
              element={
                <PrivateRoute>
                  <Artists />
                </PrivateRoute>
              }
            />
            <Route
              path="/genres"
              element={
                <PrivateRoute>
                  <Genres />
                </PrivateRoute>
              }
            />
            <Route
              path="/collections"
              element={
                <PrivateRoute>
                  <Collections />
                </PrivateRoute>
              }
            />
        </Routes>
      </main>
      <Footer />
    </div>
    </AppProvider>
  );
}

export default App;
