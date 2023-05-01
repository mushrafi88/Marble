local status_ok, lsp_installer = pcall(require,"nvim-lsp-installer")
if not status_ok then
  return 
end

--Registar a handler that will be called for all installed servers 
--ALternatively you may register handlers on specific server instances
--

lsp_installer.on_server_ready(function(server)
        local opts = {
        on_attach = require("venerable_white.lsp.handlers").on_attach,
        capabilities = require("venerable_white.lsp.handlers").capabilities,
        }
       -- if server.name =="jsonls" then
       --       local jsonls_opts = require("venerable_white.lsp.settings.jsonls")
       --         opts = vim.tbl_deep_extend("force", jsonls_opts, opts)
       -- end

        server:setup(opts)
end)
