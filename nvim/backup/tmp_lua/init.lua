--packer-installer


local install_path = vim.fn.stdpath("data") .. "/site/pack/packer/start/packer.nvim"

if vim.fn.empty(vim.fn.glob(install_path)) > 0 then
	packer_bootstrap =
		vim.fn.system({ "git", "clone", "--depth", "1", "https://github.com/wbthomason/packer.nvim", install_path })
	vim.cmd([[packadd packer.nvim]])
end


--packer plugins

local status, packer = pcall(require, "packer")
if not status then
	print("Packer is not installed")
	return
end

packer.startup(function(use)
        use('francoiscabrol/ranger.vim')
        use('rbgrouleff/bclose.vim')

        use('lilydjwg/colorizer')

        use('goolord/alpha-nvim')

        use('justinmk/vim-sneak')

        use('preservim/nerdtree')
        use('jupyter-vim/jupyter-vim')

        use('lervag/vimtex')
           
        use {
            'nvim-lualine/lualine.nvim',
             requires = { 'kyazdani42/nvim-web-devicons', opt = true }
            }

        use('L3MON4D3/LuaSnip')
        use('rafamadriz/friendly-snippets')


        use('ghifarit53/tokyonight-vim')
        if packer_bootstrap then
		packer.sync()
	end
end)


--settings


local g = vim.g
local o = vim.o
local opt = vim.opt


-- set leader key
g.mapleader = " "
g.maplocalleader = ' '
g.tex_flavor='latex'
g.vimtex_view_method = 'zathura'
g.vimtex_quickfix_mode=0
g.tex_conceal='abdmg'

g.vimtex_log_warning=0
g.vimtex_log_verbose=0
                
o.hidden = true                              
o.nowrap = true                              -- Display long lines as just one line      
o.pumheight = 10                        -- Makes popup menu smaller
opt.mouse = 'a'                             -- Enable your mouse
o.splitbelow = true                         -- Horizontal splits
o.splitright = true                          -- Vertical splits o.t_Co = 256             
o.conceallevel = 1                --to see markdown
o.ignorecase = true
o.hlsearch = true
o.clipboard ='unnamedplus'               -- Copy paste between vim and everything else
o.number = true
o.smarttab = true                           -- Makes tabbing smarter will realize you have 2 vs 4
o.expandtab = true

o.smartindent = true                         -- Makes indenting smart
o.autoindent = true                          -- Good auto indent
o.showmatch = true

o.nobackup = true                           -- This is recommended by coc
o.nowritebackup = true                       -- This is recommended by coc
o.updatetime=600                      -- Faster completion
o.timeoutlen=600

o.ttyfast=true
-- Stop newline continution of comments



--keymapping

-- alt = M
-- leader = space
-- ctrl = C
-- Use alt + hjkl to resize windows


local function map(m, k, v)
    vim.keymap.set(m, k, v, { silent = true })
end

map('n','<M-j>',':resize -2<CR>')
map('n','<M-k>',':resize +2<CR>')
map('n','<M-h>',':vertical resize -2<CR>')
map('n','<M-l>',':vertical resize +2<CR>')

--save
map('n','<C-s>',':w<CR>')

--quit
map('n','<C-Q>',':q<CR>')

--Better tabbing
map('n','<','<gv')
map('n','>','>gv')

--Better window navigation
map('n','<C-h>','<C-w>h')
map('n','<C-j>','<C-w>j')
map('n','<C-k>','<C-w>k')
map('n','<C-l>','<C-w>l')

--ranger
vim.g.ranger_map_keys = 0
map('n','<leader>r',':Ranger<CR>')

--nerdtree
map('n','<C-n>',':NERDTreeToggle<CR>')


require('venerable_white')
--source ~/.config/nvim/plugins/{coc.vim,lightline.vim,tokyonight.vim

---Pretty print lua table
function _G.dump(...)
    local objects = vim.tbl_map(vim.inspect, { ... })
    print(unpack(objects))
end
