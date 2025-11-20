# Script para gerar index.html completo
html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Métodos Numéricos - Guia Visual</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
</head>
<body class="bg-gray-900 text-gray-100 font-sans antialiased overflow-hidden">
    <div class="flex h-screen">
        <!-- Sidebar -->
        <aside class="w-64 bg-gray-800/50 backdrop-blur-md border-r border-gray-700 flex flex-col">
            <div class="p-6 border-b border-gray-700">
                <h1 class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-blue-500">
                    Métodos Numéricos
                </h1>
                <p class="text-xs text-gray-400 mt-1">Visualização Interativa</p>
            </div>
            
            <nav class="flex-1 overflow-y-auto py-4">
                <ul class="space-y-1 px-3">
                    <li>
                        <button onclick="showSection('intro')" class="nav-btn w-full text-left px-4 py-3 rounded-lg hover:bg-gray-700/50 transition-all text-gray-300 hover:text-white active-nav" id="btn-intro">
                            🏠 Introdução
                        </button>
                    </li>
                    <li>
                        <button onclick="showSection('linear')" class="nav-btn w-full text-left px-4 py-3 rounded-lg hover:bg-gray-700/50 transition-all text-gray-300 hover:text-white" id="btn-linear">
                            🧮 Sistemas Lineares (LU)
                        </button>
                    </li>
                    <li>
                        <button onclick="showSection('leastsquares')" class="nav-btn w-full text-left px-4 py-3 rounded-lg hover:bg-gray-700/50 transition-all text-gray-300 hover:text-white" id="btn-leastsquares">
                            📏 Mínimos Quadrados
                        </button>
                    </li>
                    <li>
                        <button onclick="showSection('interpolation')" class="nav-btn w-full text-left px-4 py-3 rounded-lg hover:bg-gray-700/50 transition-all text-gray-300 hover:text-white" id="btn-interpolation">
                            📈 Interpolação
                        </button>
                    </li>
                    <li>
                        <button onclick="showSection('optimization')" class="nav-btn w-full text-left px-4 py-3 rounded-lg hover:bg-gray-700/50 transition-all text-gray-300 hover:text-white" id="btn-optimization">
                            🎯 Otimização
                        </button>
                    </li>
                    <li>
                        <button onclick="showSection('markov')" class="nav-btn w-full text-left px-4 py-3 rounded-lg hover:bg-gray-700/50 transition-all text-gray-300 hover:text-white" id="btn-markov">
                            🎲 Cadeias de Markov
                        </button>
                    </li>
                    <li>
                        <button onclick="showSection('autodiff')" class="nav-btn w-full text-left px-4 py-3 rounded-lg hover:bg-gray-700/50 transition-all text-gray-300 hover:text-white" id="btn-autodiff">
                            ∂ Diferenciação Auto
                        </button>
                    </li>
                    <li>
                        <button onclick="showSection('dynamics')" class="nav-btn w-full text-left px-4 py-3 rounded-lg hover:bg-gray-700/50 transition-all text-gray-300 hover:text-white" id="btn-dynamics">
                            🦠 Sistemas Dinâmicos
                        </button>
                    </li>
                    <li class="pt-3 border-t border-gray-700 mt-3">
                        <button onclick="showSection('examples')" class="nav-btn w-full text-left px-4 py-3 rounded-lg bg-gradient-to-r from-purple-500/20 to-pink-500/20 hover:from-purple-500/30 hover:to-pink-500/30 transition-all text-white font-semibold" id="btn-examples">
                            📊 Exemplos & Resultados
                        </button>
                    </li>
                </ul>
            </nav>

            <div class="p-4 border-t border-gray-700 text-xs text-gray-500 text-center">
                Gerado por Antigravity AI
            </div>
        </aside>

        <!-- Main Content -->
        <main class="flex-1 overflow-y-auto bg-gradient-to-br from-gray-900 to-gray-800 p-8 relative">
            <!-- NOTE: All sections will be loaded from the backup file -->
            <div id="content-placeholder">
                <p class="text-white">Carregando conteúdo...</p>
            </div>
        </main>
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

# Salvar o arquivo
with open('index_temp.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Arquivo index_temp.html criado com sucesso!")
print("Agora preciso adicionar as seções do arquivo de backup...")
