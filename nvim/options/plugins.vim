call plug#begin("~/.vim/plugged")

Plug 'neoclide/coc.nvim', {'branch': 'release'}
source ~/.config/nvim/plugins/coc.vim

Plug 'itchyny/lightline.vim'
source ~/.config/nvim/plugins/lightline.vim

Plug 'francoiscabrol/ranger.vim'
Plug 'rbgrouleff/bclose.vim'

Plug 'lilydjwg/colorizer'

Plug 'goolord/alpha-nvim'

Plug 'justinmk/vim-sneak'

Plug 'preservim/nerdtree'
Plug 'jupyter-vim/jupyter-vim'

Plug 'lervag/vimtex'

Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-cmdline'

Plug 'L3MON4D3/LuaSnip'
Plug 'saadparwaiz1/cmp_luasnip'
Plug 'rafamadriz/friendly-snippets'
Plug 'f3fora/cmp-spell'

Plug 'williamboman/nvim-lsp-installer'
Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/cmp-nvim-lsp'

Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && yarn install' }

Plug 'RRethy/vim-illuminate'

Plug 'ghifarit53/tokyonight-vim'

source ~/.config/nvim/plugins/tokyonight.vim

call plug#end()

lua require'alpha'.setup(require'alpha.themes.dashboard'.opts)
