import { useState } from 'react'
import './App.css'

const AnimatedIcon = ({ type }: { type: string }) => {
  const isSunny = ["Clear", "Sunny", "Ensolarado"].some(s => type.includes(s));
  const isRainy = ["Rain", "Chuva", "Storm"].some(s => type.includes(s));

  if (isSunny && !isRainy) {
    return (
      <svg width="120" height="120" viewBox="0 0 24 24" fill="none" className="icon-sun">
        <circle cx="12" cy="12" r="5" fill="#facc15" />
        <g stroke="#facc15" strokeWidth="2" strokeLinecap="round">
          {[...Array(8)].map((_, i) => (
            <line key={i} x1="12" y1="1" x2="12" y2="3" transform={`rotate(${i * 45} 12 12)`} />
          ))}
        </g>
      </svg>
    )
  }

  return (
    <svg width="120" height="120" viewBox="0 0 24 24" fill="none" className="icon-cloud">
      <path d="M18 10c0-3.3-2.7-6-6-6s-6 2.7-6 6c-2.2 0-4 1.8-4 4s1.8 4 4 4h12c2.2 0 4-1.8 4-4s-1.8-4-4-4z" fill="#94a3b8" />
      <g stroke="#3b82f6" strokeWidth="2" strokeLinecap="round" className="icon-rain">
        <line x1="8" y1="19" x2="8" y2="21" />
        <line x1="12" y1="19" x2="12" y2="21" />
        <line x1="16" y1="19" x2="16" y2="21" />
      </g>
    </svg>
  );
};

interface Forecast {
  time: string;
  temp: number;
}

interface WeatherData {
  city: string;
  temperature: number;
  description: string;
  humidity: number;
  wind_speed: number;
  hourly: Forecast[];
}

// const MOCK_DATA: WeatherData = {
//   city: "Mogi das Cruzes",
//   temperature: 22,
//   description: "Ensolarado", /*Parcialmente Nublado, Nublado, Chuva, Tempestade, Neve*/
//   humidity: 75,
//   wind_speed: 10,
//   hourly: [
//     { time: "10:00", temp: 22 },
//     { time: "11:00", temp: 23 },
//     { time: "12:00", temp: 24 },
//     { time: "13:00", temp: 25 },
//     { time: "14:00", temp: 26 },
//   ]
// }

const weatherTranslations: Record<string, string> = {
  "Clear": "Céu Limpo",
  "Sunny": "Ensolarado",
  "Partially cloudy": "Parcialmente Nublado",
  "Cloudy": "Nublado",
  "Overcast": "Encoberto",
  "Rain": "Chuva",
  "Rain, Overcast": "Chuva",
  "Rain, Partially cloudy": "Chuva com Sol",
  "Snow": "Neve",
}

function App() {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState<WeatherData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const handleSearch = async () => {
    if (!city) return;
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`http://127.0.0.1:8000/weather/${city}`);
      if (!response.ok) throw new Error("Cidade não encontrada");
      const data = await response.json();
      setWeather(data);
    } catch (err) {
      setError("Erro ao buscar clima. Verifique o nome da cidade.")
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h2 className="main-title">Clima Geral</h2>
      <div className="bg-text">Clima</div>
      <div className="search-container">
        <div className="search-box">
          <input type="text" placeholder="Digite o nome da cidade..." value={city} onChange={(e) => setCity(e.target.value)}/>
          <button className="boton-elegante" onClick={handleSearch}>Buscar</button>
        </div>
      </div>

      {loading && <div className="btn-shine">Buscando dados em tempo real...</div>}
      {error && <p style={{ textAlign: 'center', color: 'red' }}>{error}</p>}

      {weather && (
        <div className="main-content">
          {/* Card Hero Estilo Dribbble */}
          <div className="glass-card hero-card">
            <div className="hero-content">
              <div className="hero-left">
              <AnimatedIcon type={weather.description} />
              <div>
                <p className="city-name">{weather.city}</p>
                <p className="description">{weatherTranslations[weather.description] ||weather.description}</p>
              </div>
            </div>
            <div className="hero-right">
              <h1 className="temp-main">{weather.temperature}°</h1>
            </div>
            </div>
          </div>
        
          <div className="weather-details">
            <div className="glass-card">
              <span className="label">Umidade</span>
              <span className="value">{weather.humidity}%</span>
            </div>
            <div className="glass-card">
              <span className="label">Velocidade do Vento</span>
              <span className="value">{weather.wind_speed}km/h</span>
            </div>
            {/* <div className="glass-card" style={{ gridColumn: 'span 2'}}>
              <span className="label">Previsão Horária</span>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '1rem' }}>
                {weather.hourly.map((h, i) => (
                  <div key={i} style={{ textAlign: 'center' }}>
                    <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>{h.time}</span>
                    <div style={{ fontWeight: '600', marginTop: '0.5rem' }}>{h.temp}°</div>
                  </div>
                ))}
              </div>
            </div> */}
          </div>
        </div>
      )}
    </div>
  )
}
export default App