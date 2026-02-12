# 🌿 BioNutra — Integrated Biogas & Nutrient-Rich Manure Production System

> AI-powered platform that converts agricultural waste into biogas, analyzes digested slurry nutrients, and predicts optimal fertilizer requirements for legume crops.

---

## 📖 Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture & Tech Stack](#architecture--tech-stack)
3. [Core Features](#core-features)
4. [ML Model Documentation](#ml-model-documentation)
5. [Sample Datasets](#sample-datasets)
6. [API Endpoints](#api-endpoints)
7. [Getting Started](#getting-started)
8. [Deployment](#deployment)
9. [Multi-Language Support](#multi-language-support)
10. [Project Structure](#project-structure)

---

## Project Overview

BioNutra is a full-stack, mobile-first web application designed for rural Indian farmers. It integrates three core AI prediction engines:

| Engine | Input | Output |
|---|---|---|
| **Biogas Yield Predictor** | Waste type, quantity, digester size, climate | Daily/weekly m³, energy equivalents |
| **Nutrient Analyzer** | Digested slurry composition, soil pH | N/P/K %, suitability score, curing time |
| **Fertilizer Calculator** | Crop requirements vs. manure supply | Deficit, external fertilizer recommendations, cost/savings |

---

## Architecture & Tech Stack

```
┌──────────────────────────────────────────────────────┐
│                   FRONTEND (React.js)                 │
│  ┌──────────┐ ┌──────────┐ ┌─────────┐ ┌──────────┐ │
│  │Dashboard │ │Farm Input│ │ Charts  │ │ Reports  │ │
│  └────┬─────┘ └────┬─────┘ └────┬────┘ └────┬─────┘ │
│       └─────────────┴────────────┴────────────┘      │
│                      │ REST API                       │
└──────────────────────┼────────────────────────────────┘
                       ▼
┌──────────────────────────────────────────────────────┐
│               BACKEND (Node.js / Express)             │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐  │
│  │ Auth Service│  │ Prediction   │  │ Report Gen  │  │
│  │ (JWT)       │  │ Engine (ML)  │  │ (PDF)       │  │
│  └─────────────┘  └──────┬───────┘  └─────────────┘  │
│                          │                            │
└──────────────────────────┼────────────────────────────┘
                           ▼
┌──────────────────────────────────────────────────────┐
│                    DATABASE LAYER                     │
│  PostgreSQL (primary) │ Redis (cache) │ CSV (seeds)  │
└──────────────────────────────────────────────────────┘
```

| Layer | Technology |
|---|---|
| Frontend | React.js, Tailwind CSS, Recharts |
| Backend | Node.js, Express.js |
| Database | PostgreSQL (prod), SQLite (dev) |
| ML Engine | TensorFlow.js (browser), scikit-learn (server fallback) |
| Auth | JWT + bcrypt |
| Charts | Recharts (BarChart, PieChart, RadarChart) |
| PDF Reports | jsPDF + html2canvas |
| Deployment | Docker, Vercel (frontend), Railway/Heroku (backend) |
| i18n | Custom JSON translation system |

---

## Core Features

### 1. Farm Input Module
- Waste type selector: Cow Dung, Crop Residue, Poultry Litter, Mixed
- Numeric inputs: quantity (kg), digester size (m³), acreage (ha)
- Climate zone dropdown: Tropical, Subtropical, Arid, Temperate
- Soil test fields: Nitrogen (kg/ha), pH
- Crop type selector (legumes only): Chickpea, Lentil, Soybean, Peanut, Mung Bean
- Real-time validation with prediction trigger on save

### 2. Biogas Yield Prediction
- **Daily & weekly production** estimates in cubic meters
- **Energy equivalents**: cooking hours/day, electricity generation (kWh/day)
- **7-day forecast chart** with predicted vs. actual comparison bars
- **Maintenance scheduling**: calculates next digester inspection date based on usage intensity

### 3. Manure & Nutrient Analysis
- NPK percentage estimation from digested slurry
- **Suitability score** (0–100) for legume crop compatibility
- **Curing time calculator** — varies by climate zone (14–28 days)
- Pie chart for NPK distribution; progress bars for nutrient levels
- Radar chart overlay for quick visual assessment

### 4. Fertilizer Requirement Calculator
- **Nutrient shortfall analysis**: compares manure supply against crop requirements per hectare
- **External fertilizer recommendations**: Urea (N), DAP (P), MuOP (K) with quantities in kg
- **Cost analysis**: per-product cost at Indian market rates (₹/kg)
- **Savings projection**: annual rupee savings vs. buying all fertilizer externally
- Grouped bar chart: Manure Supply vs. Crop Need vs. Deficit

### 5. Dashboard & Reports
- Summary stat cards (biogas, energy, nutrient score, electricity)
- Recent activity feed (IoT-ready event log)
- Quick NPK overview bars
- Prediction history table with date, biogas yield, score, and status
- PDF report generation (simulated in artifact; production uses jsPDF)

---

## ML Model Documentation

### Biogas Yield Model

**Algorithm**: Weighted linear regression with climate and digester efficiency multipliers.

```
daily_output = waste_qty × base_rate[waste_type]
             × climate_multiplier[climate]
             × digester_efficiency_factor

digester_efficiency = min(1.0, digester_size / 25)
efficiency_factor   = 0.7 + (digester_efficiency × 0.3)
```

| Waste Type | Base Rate (m³/kg/day) |
|---|---|
| Cow Dung | 0.035 |
| Crop Residue | 0.022 |
| Poultry Litter | 0.045 |
| Mixed | 0.030 |

| Climate Zone | Multiplier |
|---|---|
| Tropical | 1.15 |
| Subtropical | 1.05 |
| Arid | 0.78 |
| Temperate | 0.92 |

**Energy Conversion Factors:**
- 1 m³ biogas ≈ 2.8 cooking hours
- 1 m³ biogas ≈ 1.6 kWh electricity

### Nutrient Prediction Model

**Algorithm**: Baseline NPK lookup per waste type, adjusted by digestion factor and soil pH.

```
N = base_N[waste_type] × 0.82 × (0.9 + pH × 0.02)
P = base_P[waste_type] × 0.82 × 1.1
K = base_K[waste_type] × 0.82 × 1.05

suitability = min(100, N×25 + P×20 + K×15 + pH_bonus)
pH_bonus = 15 if 6.0 ≤ pH ≤ 7.5, else 0
```

| Waste Type | N (%) | P (%) | K (%) |
|---|---|---|---|
| Cow Dung | 1.80 | 0.60 | 1.20 |
| Crop Residue | 1.20 | 0.40 | 0.90 |
| Poultry Litter | 2.80 | 1.20 | 0.80 |
| Mixed | 1.60 | 0.70 | 1.00 |

### Fertilizer Calculator

**Algorithm**: Deficit = (Crop requirement × acreage) − (Manure nutrient × acreage × utilization factor)

| Crop | N req (kg/ha) | P req (kg/ha) | K req (kg/ha) |
|---|---|---|---|
| Chickpea | 3.2 | 2.8 | 1.5 |
| Lentil | 2.8 | 2.4 | 1.2 |
| Soybean | 3.8 | 3.0 | 2.0 |
| Peanut | 2.5 | 2.2 | 1.8 |
| Mung Bean | 2.2 | 1.8 | 1.0 |

**Utilization Factors**: N = 0.60, P = 0.55, K = 0.70

**Fertilizer Costs (Indian market, ₹/kg)**:
- Urea (N source): ₹22/kg
- DAP (P source): ₹35/kg
- MuOP (K source): ₹28/kg

---

## Sample Datasets

### Farmer Profile Sample
```json
{
  "id": "FRM-2026-001",
  "name": "Rajesh Kumar",
  "location": { "state": "Karnataka", "district": "Davangere", "village": "Holasamudra" },
  "farm": {
    "acreage_ha": 2.5,
    "primary_crop": "chickpea",
    "waste_type": "cow_dung",
    "daily_waste_kg": 60,
    "digester_size_m3": 25,
    "climate_zone": "tropical"
  },
  "soil_test": {
    "nitrogen_kg_ha": 14,
    "phosphorus_kg_ha": 8,
    "potassium_kg_ha": 12,
    "ph": 6.9,
    "last_tested": "2026-01-15"
  }
}
```

### Historical Prediction Log Sample
```json
[
  { "date": "2026-01-28", "biogas_m3": 3.42, "nutrient_score": 78, "status": "complete" },
  { "date": "2026-01-25", "biogas_m3": 3.18, "nutrient_score": 74, "status": "complete" },
  { "date": "2026-01-22", "biogas_m3": 3.55, "nutrient_score": 81, "status": "complete" },
  { "date": "2026-01-19", "biogas_m3": 2.98, "nutrient_score": 71, "status": "complete" },
  { "date": "2026-01-15", "biogas_m3": 3.61, "nutrient_score": 82, "status": "complete" }
]
```

### Biogas Forecast Sample Output
```json
{
  "daily_m3": 2.89,
  "weekly_m3": 20.23,
  "cooking_hours": 8.1,
  "electricity_kwh": 4.62,
  "maintenance_days": 5,
  "forecast_7d": [
    { "day": "Mon", "predicted": 2.54, "actual": 2.61 },
    { "day": "Tue", "predicted": 2.89, "actual": 2.78 },
    { "day": "Wed", "predicted": 3.24, "actual": null },
    { "day": "Thu", "predicted": 2.72, "actual": null }
  ]
}
```

---

## API Endpoints

> These endpoints are the contract for the full backend implementation. The React artifact includes the prediction logic client-side for standalone demo use.

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register` | Create farmer account |
| POST | `/api/auth/login` | Authenticate, receive JWT |
| GET | `/api/farmer/profile` | Get current farmer profile |
| PUT | `/api/farmer/profile` | Update farm details |
| POST | `/api/predict/biogas` | Run biogas yield prediction |
| POST | `/api/predict/nutrients` | Run manure nutrient analysis |
| POST | `/api/predict/fertilizer` | Run fertilizer calculator |
| GET | `/api/history` | Get prediction history |
| POST | `/api/reports/generate` | Generate PDF report |
| GET | `/api/health` | Health check |

---

## Getting Started

### Prerequisites
- Node.js ≥ 18
- npm ≥ 9
- PostgreSQL ≥ 14 (production) or SQLite (development)

### Installation

```bash
# Clone repository
git clone https://github.com/bionutra/bionutra-system.git
cd bionutra-system

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env with your DATABASE_URL, JWT_SECRET, etc.

# Run database migrations
npm run migrate

# Seed sample data
npm run seed

# Start development server
npm run dev
# Frontend: http://localhost:3000
# Backend API: http://localhost:3001
```

### Environment Variables
```env
# .env
PORT=3001
DATABASE_URL=postgresql://user:pass@localhost:5432/bionutra
JWT_SECRET=your_32_char_secret_here
JWT_EXPIRY=7d
CORS_ORIGIN=http://localhost:3000
```

---

## Deployment

### Docker (Full Stack)
```bash
# Build and run everything
docker-compose up --build

# Production build only
docker-compose -f docker-compose.prod.yml up --build -d
```

**docker-compose.yml** (reference):
```yaml
version: '3.8'
services:
  frontend:
    build: ./frontend
    ports: ["3000:3000"]
    depends_on: [backend]
  backend:
    build: ./backend
    ports: ["3001:3001"]
    environment:
      - DATABASE_URL=postgresql://db:5432/bionutra
    depends_on: [db]
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: bionutra
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

### Vercel (Frontend)
```bash
cd frontend
vercel deploy
# Set NEXT_PUBLIC_API_URL=https://your-backend.railway.app
```

### Railway (Backend + Database)
1. Connect your GitHub repo
2. Railway auto-detects Node.js
3. Add PostgreSQL add-on (connection string auto-populated)
4. Set environment variables in Railway dashboard

---

## Multi-Language Support

The app ships with three languages out of the box:

| Language | Code | Coverage |
|---|---|---|
| English | `en` | Full |
| Hindi (हिन्दी) | `hi` | Full |
| Kannada (ಕನ್ನಡ) | `ka` | Full |

### Adding a New Language
1. Create a new key in the `i18n` object in `src/i18n/translations.js`
2. Copy the `en` structure as a template
3. Translate all string values
4. Add the language option to the header dropdown

---

## Project Structure

```
bionutra-system/
├── frontend/
│   ├── src/
│   │   ├── App.jsx                  # Main application shell
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx        # Home dashboard
│   │   │   ├── FarmInput.jsx        # Input form module
│   │   │   ├── BiogasYield.jsx      # Biogas predictions + chart
│   │   │   ├── ManureAnalysis.jsx   # NPK analysis + charts
│   │   │   ├── FertilizerCalc.jsx   # Fertilizer calculator
│   │   │   └── Reports.jsx          # Report generation + history
│   │   ├── ml/
│   │   │   ├── biogasModel.js       # Biogas yield prediction engine
│   │   │   ├── nutrientModel.js     # Nutrient prediction engine
│   │   │   └── fertilizerModel.js   # Fertilizer calculator engine
│   │   ├── i18n/
│   │   │   └── translations.js      # en, hi, ka translations
│   │   ├── components/
│   │   │   ├── StatCard.jsx         # Metric display card
│   │   │   ├── NutrientBar.jsx      # Progress bar component
│   │   │   └── SectionHeader.jsx    # Page section header
│   │   └── utils/
│   │       └── pdfReport.js         # PDF generation (jsPDF)
│   ├── public/
│   └── package.json
├── backend/
│   ├── src/
│   │   ├── index.js                 # Express app entry
│   │   ├── routes/
│   │   │   ├── auth.js              # Login/register
│   │   │   ├── predict.js           # ML prediction endpoints
│   │   │   └── reports.js           # PDF generation
│   │   ├── middleware/
│   │   │   └── authMiddleware.js    # JWT verification
│   │   ├── models/
│   │   │   └── farmer.js            # Sequelize/Prisma model
│   │   └── ml/
│   │       ├── biogasModel.py       # scikit-learn model (optional)
│   │       └── train.py             # Model training script
│   └── package.json
├── data/
│   ├── farmers_sample.json          # Sample farmer profiles
│   ├── history_sample.json          # Historical predictions
│   └── crop_requirements.json       # NPK requirements per crop
├── docker-compose.yml
├── docker-compose.prod.yml
├── .env.example
└── README.md                        # This file
```

---

## License
MIT — Free to use for agricultural and educational purposes.

## Contact
BioNutra Project Team — Open an issue or PR on GitHub.
