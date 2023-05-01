source ~/.config/nvim/options/settings.vim
source ~/.config/nvim/options/keys.vim
source ~/.config/nvim/options/plugins.vim

lua require("luasnip.loaders.from_vscode").lazy_load()
"lua require("luasnip.loaders.from_vscode").load({ paths = "~/.config/nvim/snippets"})
lua require("venerable_white")

colorscheme tokyonight
