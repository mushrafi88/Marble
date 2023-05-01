" set leader key
let g:mapleader = "\<Space>"
let g:tex_flavor='latex'
let g:vimtex_view_method = 'zathura'
let g:vimtex_quickfix_mode=0
let g:tex_conceal='abdmg'

let g:vimtex_log_warning=0
let g:vimtex_log_verbose=0

filetype plugin indent on
syntax enable                           " Enables syntax highlighing
set hidden                              " Required to keep multiple buffers open multiple buffers
"set nowrap                              " Display long lines as just one line
set encoding=utf-8                      " The encoding displayed
set pumheight=10                        " Makes popup menu smaller
set fileencoding=utf-8                  " The encoding written to file
set iskeyword+=-                      	" treat dash separated words as a word text object"
set mouse=a                             " Enable your mouse
set splitbelow                          " Horizontal splits will automatically be below
set splitright                          " Vertical splits will automatically be to the right
set t_Co=256                            " Support 256 colors
set conceallevel=1                     " So that I can see `` in markdown files                         " Converts tabs to spaces
set ignorecase
set hlsearch
set incsearch
set clipboard=unnamedplus               " Copy paste between vim and everything else
set number number
set smarttab                            " Makes tabbing smarter will realize you have 2 vs 4
set expandtab 

set smartindent                         " Makes indenting smart
set autoindent                          " Good auto indent
set showmatch

set nobackup                            " This is recommended by coc
set nowritebackup                       " This is recommended by coc
set updatetime=600                      " Faster completion
set timeoutlen=600

set wildmode="longest:list"               " autocomplete
set ttyfast
set formatoptions-=cro      " Stop newline continution of comments
set shell=zsh
" remove tildes
highlight! EndOfBuffer ctermfg=black
