# AI Production Planner MCP (`auto-planner-mcp`)

An Industry 4.0 AI Production Planning MCP (Model Context Protocol) Server for automotive manufacturing lines. This system provides intelligent assembly queue management, Just-In-Sequence (JIS) inventory tracking, Overall Equipment Effectiveness (OEE) analytics, and downtime financial impact estimations.

---

## 📐 Project Architecture & Structure

```text
auto-planner-mcp/
├── data/                      # Industry 4.0 Mock Datasets
│   ├── assembly_queue.json    # Active vehicle assembly queue (VINs, models, seat types)
│   ├── inventory_jit.json     # Just-In-Time/Sequence parts inventory & ETA tracking
│   └── station_oee.json       # Assembly station efficiency & operational status
├── teammates/                 # Modular Python Logic Engines
│   ├── dev_a/                 # Assembly Queue & Resequencing Engine
│   │   ├── __init__.py
│   │   └── logic.py
│   └── dev_b/                 # Inventory & OEE Analytics Engine
│       ├── __init__.py
│       └── logic.py
├── package.json               # NitroStack MCP server configuration
└── tsconfig.json              # TypeScript configuration
```

---

## ✨ Features & Functionality

### 🚘 Developer A Logic (`teammates/dev_a/logic.py`)
- **`get_assembly_sequence(shift_id: str, line_id: str)`**
  - Retrieves the active build queue for a given shift and assembly line.
- **`resequence_build_plan(delay_reason: str, missing_option: str)`**
  - Dynamically resequences the assembly plan when part shortages occur (e.g., missing seat trims) by prioritizing available configurations and placing delayed VINs at the back of the queue.

### 🏭 Developer B Logic (`teammates/dev_b/logic.py`)
- **`check_jis_inventory(part_number: str, vin_sequence: str = None)`**
  - Checks stock levels, supplier ETAs, and shortage indicators for required JIS automotive parts.
- **`calculate_station_oee(station_id: str)`**
  - Calculates Overall Equipment Effectiveness ($OEE = Availability \times Performance \times Quality$) for manufacturing stations (e.g., `STATION_WELDING`).
- **`estimate_downtime_cost(stopped_station_id: str)`**
  - Computes financial losses based on station downtime duration (assumes $\$22,000/\text{min}$ for non-running stations).

---

## 📊 Mock Data Schemas

| Dataset | File Path | Key Attributes |
| :--- | :--- | :--- |
| **Assembly Queue** | `data/assembly_queue.json` | `vin`, `model`, `trim`, `seat_type`, `status` |
| **JIT Inventory** | `data/inventory_jit.json` | `stock`, `supplier_eta`, `shortage` |
| **Station OEE** | `data/station_oee.json` | `availability`, `performance`, `quality`, `status` |

---

## 🧪 Testing & Verification

### Run Teammate Logic Verification
To test Developer A & B logic together via Python:
```bash
python3 -c "
from teammates.dev_a.logic import get_assembly_sequence, resequence_build_plan
from teammates.dev_b.logic import check_jis_inventory, calculate_station_oee, estimate_downtime_cost

print(get_assembly_sequence('SHIFT_1', 'LINE_A'))
print(resequence_build_plan('Seat Shortage', 'RED_LEATHER'))
print(check_jis_inventory('RED_LEATHER'))
print(calculate_station_oee('STATION_WELDING'))
print(estimate_downtime_cost('STATION_PAINT'))
"
```

---

## 🚀 Running the MCP Server

```bash
# Start in development mode
npm run dev

# Build the project
npm run build

# Start production server
npm start
```
