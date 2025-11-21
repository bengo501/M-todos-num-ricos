
// Global Chart Instances
let interpolationChart = null;
let optimizationChart = null;
let sirChart = null;
let leastSquaresChart = null;

// Navigation
function showSection(sectionId) {
    // Hide all sections
    document.querySelectorAll('.section-content').forEach(el => el.classList.add('hidden'));
    // Show selected
    document.getElementById(sectionId).classList.remove('hidden');
    
    // Update Nav Buttons
    document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active-nav'));
    document.getElementById('btn-' + sectionId).classList.add('active-nav');

    // Initialize Charts/Modules if needed
    if (sectionId === 'interpolation' && !interpolationChart) initInterpolation();
    if (sectionId === 'optimization' && !optimizationChart) initOptimization();
    if (sectionId === 'dynamics' && !sirChart) initSIR();
    if (sectionId === 'leastsquares' && !leastSquaresChart) initLeastSquares();
    if (sectionId === 'linear') initLinearSystems();
    if (sectionId === 'markov') initMarkov();
    if (sectionId === 'autodiff') initAutoDiff();
}

// ==========================================
// LINEAR SYSTEMS LOGIC (LU Decomposition)
// ==========================================
function initLinearSystems() {
    const container = document.getElementById('matrixA-inputs');
    if (container.innerHTML.trim() !== '') return; // Already initialized

    // Default Matrix A (Parquinho Problem)
    const defaultA = [
        [20, 10, 0],
        [10, 20, 10],
        [0, 10, 20]
    ];

    // Create Inputs
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const input = document.createElement('input');
            input.type = 'number';
            input.value = defaultA[i][j];
            input.className = 'w-full bg-gray-700 border border-gray-600 rounded px-2 py-1 text-white text-center matrix-input';
            input.dataset.row = i;
            input.dataset.col = j;
            container.appendChild(input);
        }
    }
}

function resetMatrixA() {
    const defaultA = [
        [20, 10, 0],
        [10, 20, 10],
        [0, 10, 20]
    ];
    const inputs = document.querySelectorAll('.matrix-input');
    inputs.forEach(input => {
        const r = parseInt(input.dataset.row);
        const c = parseInt(input.dataset.col);
        input.value = defaultA[r][c];
    });
    document.getElementById('matrixL-display').innerText = '';
    document.getElementById('matrixU-display').innerText = '';
}

function solveLU() {
    // Read Matrix A
    const A = [[0,0,0], [0,0,0], [0,0,0]];
    const inputs = document.querySelectorAll('.matrix-input');
    inputs.forEach(input => {
        const r = parseInt(input.dataset.row);
        const c = parseInt(input.dataset.col);
        A[r][c] = parseFloat(input.value);
    });

    // LU Decomposition Algorithm (Doolittle)
    const n = 3;
    const L = [[1,0,0], [0,1,0], [0,0,1]];
    const U = [[0,0,0], [0,0,0], [0,0,0]];

    for (let i = 0; i < n; i++) {
        // Upper Triangular
        for (let k = i; k < n; k++) {
            let sum = 0;
            for (let j = 0; j < i; j++) {
                sum += (L[i][j] * U[j][k]);
            }
            U[i][k] = A[i][k] - sum;
        }

        // Lower Triangular
        for (let k = i; k < n; k++) {
            if (i === k) {
                L[i][i] = 1;
            } else {
                let sum = 0;
                for (let j = 0; j < i; j++) {
                    sum += (L[k][j] * U[j][i]);
                }
                L[k][i] = (A[k][i] - sum) / U[i][i];
            }
        }
    }

    // Display Results
    displayMatrix('matrixL-display', L);
    displayMatrix('matrixU-display', U);
}

function displayMatrix(elementId, matrix) {
    let text = '';
    for (let i = 0; i < matrix.length; i++) {
        text += '| ';
        for (let j = 0; j < matrix[i].length; j++) {
            text += matrix[i][j].toFixed(2).padStart(6, ' ') + ' ';
        }
        text += '|\n';
    }
    document.getElementById(elementId).innerText = text;
}

// ==========================================
// LEAST SQUARES LOGIC
// ==========================================
let lsPoints = [];

function initLeastSquares() {
    const ctx = document.getElementById('leastSquaresChart').getContext('2d');
    
    leastSquaresChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'Pontos Observados',
                    data: [],
                    backgroundColor: 'yellow',
                    pointRadius: 6
                },
                {
                    label: 'Reta de Regressão',
                    data: [],
                    borderColor: 'red',
                    borderWidth: 2,
                    showLine: true,
                    pointRadius: 0,
                    fill: false,
                    type: 'line'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { min: 0, max: 10, grid: { color: '#374151' } },
                y: { min: 0, max: 10, grid: { color: '#374151' } }
            },
            onClick: (e) => {
                const canvasPosition = Chart.helpers.getRelativePosition(e, leastSquaresChart);
                const dataX = leastSquaresChart.scales.x.getValueForPixel(canvasPosition.x);
                const dataY = leastSquaresChart.scales.y.getValueForPixel(canvasPosition.y);
                
                addLSPoint(dataX, dataY);
            }
        }
    });
}

function addLSPoint(x, y) {
    lsPoints.push({x, y});
    updateLSChart();
}

function clearLeastSquares() {
    lsPoints = [];
    updateLSChart();
}

function updateLSChart() {
    // Update Points
    leastSquaresChart.data.datasets[0].data = lsPoints;

    // Calculate Regression Line (y = ax + b)
    if (lsPoints.length >= 2) {
        let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0;
        const n = lsPoints.length;

        for (let p of lsPoints) {
            sumX += p.x;
            sumY += p.y;
            sumXY += p.x * p.y;
            sumXX += p.x * p.x;
        }

        const slope = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
        const intercept = (sumY - slope * sumX) / n;

        // Generate Line Points
        const lineData = [
            {x: 0, y: intercept},
            {x: 10, y: slope * 10 + intercept}
        ];
        leastSquaresChart.data.datasets[1].data = lineData;

        // Calculate MSE
        let mse = 0;
        for (let p of lsPoints) {
            const predY = slope * p.x + intercept;
            mse += Math.pow(p.y - predY, 2);
        }
        mse /= n;

        // Update UI
        document.getElementById('ls-equation').innerText = `y = ${slope.toFixed(2)}x + ${intercept.toFixed(2)}`;
        document.getElementById('ls-error').innerText = mse.toFixed(4);
    } else {
        leastSquaresChart.data.datasets[1].data = [];
        document.getElementById('ls-equation').innerText = '-';
        document.getElementById('ls-error').innerText = '-';
    }
    
    leastSquaresChart.update();
}

// ==========================================
// INTERPOLATION LOGIC
// ==========================================
let interpPoints = [];

function initInterpolation() {
    const ctx = document.getElementById('interpolationChart').getContext('2d');
    
    interpolationChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'Pontos Dados',
                    data: [],
                    backgroundColor: 'cyan',
                    pointRadius: 6
                },
                {
                    label: 'Polinômio Interpolador',
                    data: [],
                    borderColor: 'cyan',
                    borderWidth: 2,
                    showLine: true,
                    pointRadius: 0,
                    fill: false,
                    type: 'line'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { min: -10, max: 10, grid: { color: '#374151' } },
                y: { min: -10, max: 10, grid: { color: '#374151' } }
            },
            onClick: (e) => {
                const canvasPosition = Chart.helpers.getRelativePosition(e, interpolationChart);
                const dataX = interpolationChart.scales.x.getValueForPixel(canvasPosition.x);
                const dataY = interpolationChart.scales.y.getValueForPixel(canvasPosition.y);
                
                addInterpPoint(dataX, dataY);
            }
        }
    });
}

function addInterpPoint(x, y) {
    interpPoints.push({x, y});
    interpPoints.sort((a, b) => a.x - b.x); // Sort by X
    updateInterpChart();
}

function clearInterpolation() {
    interpPoints = [];
    updateInterpChart();
}

function updateInterpChart() {
    // Update Points
    interpolationChart.data.datasets[0].data = interpPoints;

    // Calculate Polynomial Curve
    if (interpPoints.length >= 2) {
        const curveData = [];
        for (let x = -10; x <= 10; x += 0.1) {
            curveData.push({x: x, y: lagrange(x, interpPoints)});
        }
        interpolationChart.data.datasets[1].data = curveData;
    } else {
        interpolationChart.data.datasets[1].data = [];
    }
    
    interpolationChart.update();
}

function lagrange(x, points) {
    let result = 0;
    const n = points.length;
    
    for (let i = 0; i < n; i++) {
        let term = points[i].y;
        for (let j = 0; j < n; j++) {
            if (i !== j) {
                term *= (x - points[j].x) / (points[i].x - points[j].x);
            }
        }
        result += term;
    }
    return result;
}

// ==========================================
// OPTIMIZATION LOGIC (Gradient Descent)
// ==========================================
function initOptimization() {
    const ctx = document.getElementById('optimizationChart').getContext('2d');
    
    // Generate Function Curve f(x) = x^2 - 4x + 4
    const curveData = [];
    for (let x = -1; x <= 5; x += 0.1) {
        curveData.push({x: x, y: x*x - 4*x + 4});
    }

    optimizationChart = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [
                {
                    label: 'f(x) = x² - 4x + 4',
                    data: curveData,
                    borderColor: 'purple',
                    borderWidth: 2,
                    pointRadius: 0,
                    fill: false
                },
                {
                    label: 'Posição Atual',
                    data: [{x: 0, y: 4}],
                    backgroundColor: 'cyan',
                    pointRadius: 8,
                    type: 'scatter'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { grid: { color: '#374151' } },
                y: { grid: { color: '#374151' } }
            },
            animation: {
                duration: 0 // Disable default animation for manual control
            }
        }
    });
}

async function startGradientDescent() {
    const lr = parseFloat(document.getElementById('learningRate').value);
    let x = 0; // Start at 0
    let iter = 0;
    const maxIter = 20;

    // Reset
    optimizationChart.data.datasets[1].data = [{x: x, y: x*x - 4*x + 4}];
    optimizationChart.update();

    for (let i = 0; i < maxIter; i++) {
        await new Promise(r => setTimeout(r, 500)); // Delay 500ms
        
        const grad = 2*x - 4; // f'(x) = 2x - 4
        x = x - lr * grad;
        const y = x*x - 4*x + 4;

        // Update UI
        document.getElementById('opt-iter').innerText = i + 1;
        document.getElementById('opt-x').innerText = x.toFixed(4);
        document.getElementById('opt-grad').innerText = grad.toFixed(4);

        // Update Chart
        optimizationChart.data.datasets[1].data = [{x: x, y: y}];
        optimizationChart.update();

        if (Math.abs(grad) < 0.01) break;
    }
}

// ==========================================
// MARKOV CHAINS LOGIC
// ==========================================
function initMarkov() {
    // Sorveteria Simulation
    const vizContainer = document.getElementById('markov-viz');
    if (vizContainer.innerHTML.includes('Simulação em Breve')) {
        vizContainer.innerHTML = `
            <div class="flex flex-col items-center gap-4 w-full">
                <div class="flex justify-around w-full">
                    <div id="state-choc" class="p-4 bg-gray-800 rounded-full border-4 border-gray-600 transition-all duration-300">
                        🍫 Chocolate
                        <div id="prob-choc" class="text-xs text-center">50%</div>
                    </div>
                    <div id="state-van" class="p-4 bg-gray-800 rounded-full border-4 border-gray-600 transition-all duration-300">
                        🍦 Baunilha
                        <div id="prob-van" class="text-xs text-center">50%</div>
                    </div>
                </div>
                <button onclick="stepMarkov()" class="px-4 py-2 bg-pink-600 text-white rounded hover:bg-pink-700">
                    Próximo Dia (Simular)
                </button>
                <div class="text-sm text-gray-400">
                    Transição: C->C (0.7), C->B (0.3) | B->C (0.6), B->B (0.4)
                </div>
            </div>
        `;
    }
}

let currentProb = [0.5, 0.5]; // [Chocolate, Baunilha]

function stepMarkov() {
    // Transition Matrix
    // [P(C|C) P(B|C)]
    // [P(C|B) P(B|B)]
    const P = [
        [0.7, 0.3],
        [0.6, 0.4]
    ];

    // New Probabilities: v_new = v_old * P
    const newChoc = currentProb[0] * P[0][0] + currentProb[1] * P[1][0];
    const newVan = currentProb[0] * P[0][1] + currentProb[1] * P[1][1];

    currentProb = [newChoc, newVan];

    // Update UI
    document.getElementById('prob-choc').innerText = (currentProb[0] * 100).toFixed(1) + '%';
    document.getElementById('prob-van').innerText = (currentProb[1] * 100).toFixed(1) + '%';

    // Visual Feedback
    const chocEl = document.getElementById('state-choc');
    const vanEl = document.getElementById('state-van');
    
    chocEl.style.borderColor = `rgba(236, 72, 153, ${currentProb[0]})`; // Pink
    vanEl.style.borderColor = `rgba(236, 72, 153, ${currentProb[1]})`;
}

// ==========================================
// AUTO DIFFERENTIATION LOGIC
// ==========================================
function initAutoDiff() {
    updateAutoDiff();
}

function updateAutoDiff() {
    const x = parseFloat(document.getElementById('autodiff-slider').value);
    document.getElementById('autodiff-val').innerText = x.toFixed(1);

    // Function: f(x) = x^2 + sin(x)
    // Forward Pass
    const t1 = x * x;
    const t2 = Math.sin(x);
    const f = t1 + t2;

    // Backward Pass (Gradients)
    const df = 1.0;
    const dt1 = df * 1.0;
    const dt2 = df * 1.0;
    const dx_from_t1 = dt1 * 2 * x;
    const dx_from_t2 = dt2 * Math.cos(x);
    const dx = dx_from_t1 + dx_from_t2;

    // Render Graph
    const container = document.getElementById('autodiff-graph');
    container.innerHTML = `
        <div class="relative w-full h-full flex items-center justify-center">
            <!-- Nodes -->
            <div class="absolute left-10 top-1/2 transform -translate-y-1/2 bg-indigo-900 p-2 rounded border border-indigo-500 text-center w-24">
                <div class="text-xs text-gray-400">Input x</div>
                <div class="font-bold">${x.toFixed(2)}</div>
                <div class="text-xs text-indigo-300">grad: ${dx.toFixed(2)}</div>
            </div>

            <div class="absolute left-1/3 top-1/3 bg-gray-800 p-2 rounded border border-gray-600 text-center w-24">
                <div class="text-xs text-gray-400">x²</div>
                <div class="font-bold">${t1.toFixed(2)}</div>
            </div>

            <div class="absolute left-1/3 bottom-1/3 bg-gray-800 p-2 rounded border border-gray-600 text-center w-24">
                <div class="text-xs text-gray-400">sin(x)</div>
                <div class="font-bold">${t2.toFixed(2)}</div>
            </div>

            <div class="absolute right-10 top-1/2 transform -translate-y-1/2 bg-green-900 p-2 rounded border border-green-500 text-center w-24">
                <div class="text-xs text-gray-400">Output f</div>
                <div class="font-bold">${f.toFixed(2)}</div>
            </div>
            
            <!-- Connections (Simple Lines using SVG) -->
            <svg class="absolute inset-0 w-full h-full pointer-events-none" style="z-index: -1;">
                <line x1="15%" y1="50%" x2="33%" y2="35%" stroke="#4B5563" stroke-width="2" />
                <line x1="15%" y1="50%" x2="33%" y2="65%" stroke="#4B5563" stroke-width="2" />
                <line x1="45%" y1="35%" x2="80%" y2="50%" stroke="#4B5563" stroke-width="2" />
                <line x1="45%" y1="65%" x2="80%" y2="50%" stroke="#4B5563" stroke-width="2" />
            </svg>
        </div>
    `;
}

// ==========================================
// DYNAMIC SYSTEMS LOGIC (SIR & Two Tanks)
// ==========================================
function showDynamicsTab(tab) {
    const sirContainer = document.getElementById('sir-container');
    const tanksContainer = document.getElementById('tanks-container');
    const tabSir = document.getElementById('tab-sir');
    const tabTanks = document.getElementById('tab-tanks');

    if (tab === 'sir') {
        sirContainer.classList.remove('hidden');
        tanksContainer.classList.add('hidden');
        tabSir.classList.add('text-green-400', 'border-green-400');
        tabSir.classList.remove('text-gray-400', 'border-transparent');
        tabTanks.classList.add('text-gray-400', 'border-transparent');
        tabTanks.classList.remove('text-blue-400', 'border-blue-400');
    } else {
        sirContainer.classList.add('hidden');
        tanksContainer.classList.remove('hidden');
        tabTanks.classList.add('text-blue-400', 'border-blue-400');
        tabTanks.classList.remove('text-gray-400', 'border-transparent');
        tabSir.classList.add('text-gray-400', 'border-transparent');
        tabSir.classList.remove('text-green-400', 'border-green-400');
    }
}

function initSIR() {
    const ctx = document.getElementById('sirChart').getContext('2d');
    
    sirChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                { label: 'Suscetíveis', borderColor: 'cyan', data: [], pointRadius: 0 },
                { label: 'Infectados', borderColor: 'red', data: [], pointRadius: 0 },
                { label: 'Recuperados', borderColor: 'green', data: [], pointRadius: 0 }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { grid: { color: '#374151' }, title: { display: true, text: 'Dias' } },
                y: { grid: { color: '#374151' }, title: { display: true, text: 'População' } }
            },
            interaction: { mode: 'index', intersect: false }
        }
    });

    updateSIR();
}

function updateSIR() {
    const beta = parseFloat(document.getElementById('betaSlider').value);
    const gamma = parseFloat(document.getElementById('gammaSlider').value);
    
    document.getElementById('betaVal').innerText = beta.toFixed(4);
    document.getElementById('gammaVal').innerText = gamma.toFixed(2);

    // Simulation Parameters
    const N = 1000;
    let S = 990;
    let I = 10;
    let R = 0;
    const dt = 0.1;
    const days = 100;
    const steps = days / dt;

    const dataS = [];
    const dataI = [];
    const dataR = [];
    const labels = [];

    let maxI = 0;
    let maxIDay = 0;

    for (let i = 0; i < steps; i++) {
        // Euler Method
        const dS = -beta * S * I;
        const dI = beta * S * I - gamma * I;
        const dR = gamma * I;

        S += dS * dt;
        I += dI * dt;
        R += dR * dt;

        if (I > maxI) {
            maxI = I;
            maxIDay = i * dt;
        }

        if (i % 10 === 0) { // Downsample for chart performance
            dataS.push(S);
            dataI.push(I);
            dataR.push(R);
            labels.push((i * dt).toFixed(0));
        }
    }

    // Update UI Stats
    document.getElementById('sirPeak').innerText = Math.round(maxI);
    document.getElementById('sirPeakDay').innerText = maxIDay.toFixed(1);

    // Update Chart
    sirChart.data.labels = labels;
    sirChart.data.datasets[0].data = dataS;
    sirChart.data.datasets[1].data = dataI;
    sirChart.data.datasets[2].data = dataR;
    sirChart.update();
}

async function startTwoTanks() {
    // Simulation: Salt concentration exchange
    // x1' = -k1*x1 + k2*x2
    // x2' = k1*x1 - k2*x2
    
    let x1 = 100; // Initial salt in T1
    let x2 = 0;   // Initial salt in T2
    const k = 0.05; // Exchange rate
    const dt = 0.1;
    const steps = 200;

    const t1Water = document.getElementById('tank1-water');
    const t2Water = document.getElementById('tank2-water');
    const t1Conc = document.getElementById('tank1-conc');
    const t2Conc = document.getElementById('tank2-conc');

    for (let i = 0; i < steps; i++) {
        const dx1 = -k * x1 + k * x2;
        const dx2 = k * x1 - k * x2;

        x1 += dx1 * dt;
        x2 += dx2 * dt;

        // Update Visuals
        // Opacity based on concentration (max 100)
        t1Water.style.backgroundColor = `rgba(59, 130, 246, ${0.2 + (x1/150)})`; 
        t2Water.style.backgroundColor = `rgba(59, 130, 246, ${0.2 + (x2/150)})`;
        
        t1Conc.innerText = x1.toFixed(1) + ' kg';
        t2Conc.innerText = x2.toFixed(1) + ' kg';

        await new Promise(r => setTimeout(r, 20)); // Animation speed
    }
}

// ==========================================
// EXAMPLES SECTION CHARTS
// ==========================================

// Global chart instances for examples section
let exampleCharts = {
    linear: null,
    leastSquares: null,
    markov: null,
    interpolation: null,
    optimization: null,
    autodiff: null,
    dynamics: null
};

// Modify showSection to initialize example charts when Examples section is shown
const originalShowSection = showSection;
showSection = function(sectionId) {
    originalShowSection(sectionId);
    if (sectionId === 'examples') {
        setTimeout(() => {
            if (!exampleCharts.linear) initAllExampleCharts();
        }, 100);
    }
};

// Initialize all example charts
function initAllExampleCharts() {
    initChartLinear();
    initChartLeastSquares();
    initChartMarkov();
    initChartInterpolation();
    initChartOptimization();
    initChartAutoDiff();
    initChartDynamics();
}

// 1. Linear Systems Chart (Bar chart of solution)
function initChartLinear() {
    const ctx = document.getElementById('chartLinear');
    if (!ctx) return;
    exampleCharts.linear = new Chart(ctx.getContext('2d'), {
        type: 'bar',
        data: {
            labels: ['Brinquedo 1', 'Brinquedo 2', 'Brinquedo 3'],
            datasets: [{
                label: 'Fluxo de Crianças',
                data: [6.67, 11.67, 4.17],
                backgroundColor: ['#60a5fa', '#34d399', '#fbbf24']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Solução do Sistema Linear (Fluxo nos Brinquedos)',
                    color: '#fff'
                },
                legend: { labels: { color: '#fff' } }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: { display: true, text: 'Fluxo', color: '#fff' },
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                },
                x: {
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                }
            }
        }
    });
}

// 2. Least Squares Chart (Observed vs Predicted)
function initChartLeastSquares() {
    const ctx = document.getElementById('chartLeastSquares');
    if (!ctx) return;
    exampleCharts.leastSquares = new Chart(ctx.getContext('2d'), {
        type: 'bar',
        data: {
            labels: ['Amostra 1', 'Amostra 2', 'Amostra 3'],
            datasets: [
                {
                    label: 'Observado',
                    data: [24.3, 15.0, 26.2],
                    backgroundColor: '#60a5fa'
                },
                {
                    label: 'Predito',
                    data: [24.3, 15.45, 26.25],
                    backgroundColor: '#34d399'
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Análise Química: Observado vs Predito',
                    color: '#fff'
                },
                legend: { labels: { color: '#fff' } }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: { display: true, text: 'Concentração (%)', color: '#fff' },
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                },
                x: {
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                }
            }
        }
    });
}

// 3. Markov Chains Chart (Steady state probabilities)
function initChartMarkov() {
    const ctx = document.getElementById('chartMarkov');
    if (!ctx) return;
    exampleCharts.markov = new Chart(ctx.getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Preferem Sim (66.67%)', 'Preferem Não (33.33%)'],
            datasets: [{
                data: [66.67, 33.33],
                backgroundColor: ['#ec4899', '#8b5cf6']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Estado Estacionário - Sorveteria',
                    color: '#fff'
                },
                legend: { labels: { color: '#fff' } }
            }
        }
    });
}

// 4. Interpolation Chart (Data points and curve)
function initChartInterpolation() {
    const ctx = document.getElementById('chartInterpolation');
    if (!ctx) return;
    
    const years = [1990, 1991, 1992, 1993, 1994, 1995, 1996];
    const production = [62.4, 67.7, 75.9, 87.4, 97.4, 105.3, 113.2];
    
    exampleCharts.interpolation = new Chart(ctx.getContext('2d'), {
        type: 'line',
        data: {
            labels: years,
            datasets: [{
                label: 'Produção de Aço (Lagrange)',
                data: production,
                borderColor: '#06b6d4',
                backgroundColor: 'rgba(6, 182, 212, 0.1)',
                pointRadius: 5,
                pointBackgroundColor: '#06b6d4',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Interpolação de Lagrange - Produção de Aço',
                    color: '#fff'
                },
                legend: { labels: { color: '#fff' } }
            },
            scales: {
                y: {
                    title: { display: true, text: 'Produção (milhões ton)', color: '#fff' },
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                },
                x: {
                    title: { display: true, text: 'Ano', color: '#fff' },
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                }
            }
        }
    });
}

// 5. Optimization Chart (Convergence)
function initChartOptimization() {
    const ctx = document.getElementById('chartOptimization');
    if (!ctx) return;
    
    const iterations = Array.from({length: 21}, (_, i) => i);
    const fVals = [];
    let x = 0;
    for (let i = 0; i < 21; i++) {
        fVals.push(x**2 - 4*x + 4);
        x = x - 0.1 * (2*x - 4);
    }
    
    exampleCharts.optimization = new Chart(ctx.getContext('2d'), {
        type: 'line',
        data: {
            labels: iterations,
            datasets: [{
                label: 'f(x) = x² - 4x + 4',
                data: fVals,
                borderColor: '#a855f7',
                backgroundColor: 'rgba(168, 85, 247, 0.1)',
                pointRadius: 3,
                fill: true
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Convergência do Gradiente Descendente',
                    color: '#fff'
                },
                legend: { labels: { color: '#fff' } }
            },
            scales: {
                y: {
                    title: { display: true, text: 'f(x)', color: '#fff' },
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                },
                x: {
                    title: { display: true, text: 'Iteração', color: '#fff' },
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                }
            }
        }
    });
}

// 6. AutoDiff Chart (Partial derivatives)
function initChartAutoDiff() {
    const ctx = document.getElementById('chartAutoDiff');
    if (!ctx) return;
    exampleCharts.autodiff = new Chart(ctx.getContext('2d'), {
        type: 'bar',
        data: {
            labels: ['∂f/∂x', '∂f/∂y', '∂f/∂z'],
            datasets: [{
                label: 'Derivadas Parciais',
                data: [5.2, 4.4, -3.44],
                backgroundColor: ['#6366f1', '#8b5cf6', '#ec4899']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Derivadas Parciais em (2, 3, 5)',
                    color: '#fff'
                },
                legend: { labels: { color: '#fff' } }
            },
            scales: {
                y: {
                    title: { display: true, text: 'Valor da Derivada', color: '#fff' },
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                },
                x: {
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                }
            }
        }
    });
}

// 7. Dynamic Systems Chart (Tanks over time)
function initChartDynamics() {
    const ctx = document.getElementById('chartDynamics');
    if (!ctx) return;
    
    // Generate tank dynamics data
    const time = [];
    const tankA = [];
    const tankB = [];
    let x = 100, y = 0;
    for (let t = 0; t <= 50; t++) {
        time.push(t);
        tankA.push(x);
        tankB.push(y);
        for (let i = 0; i < 10; i++) {
            const dx = 0.05*y - 0.1*x;
            const dy = 0.1*x - 0.05*y;
            x += dx * 0.1;
            y += dy * 0.1;
        }
    }
    
    exampleCharts.dynamics = new Chart(ctx.getContext('2d'), {
        type: 'line',
        data: {
            labels: time,
            datasets: [
                {
                    label: 'Tanque A (sal)',
                    data: tankA,
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    pointRadius: 0,
                    borderWidth: 2
                },
                {
                    label: 'Tanque B (sal)',
                    data: tankB,
                    borderColor: '#3b82f6',
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
                    pointRadius: 0,
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Dois Tanques - Dinâmica do Sistema',
                    color: '#fff'
                },
                legend: { labels: { color: '#fff' } }
            },
            scales: {
                y: {
                    title: { display: true, text: 'Quantidade de Sal (kg)', color: '#fff' },
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                },
                x: {
                    title: { display: true, text: 'Tempo (s)', color: '#fff' },
                    ticks: { color: '#fff' },
                    grid: { color: '#374151' }
                }
            }
        }
    });
}
