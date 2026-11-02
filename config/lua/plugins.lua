local ensure_packer = function()
	local fn = vim.fn
	local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
	if fn.empty(fn.glob(install_path)) > 0 then
		fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
		vim.cmd [[packadd packer.nvim]]
	return true
	end
	return false
end

local packer_bootstrap = ensure_packer()

return require('packer').startup(function(use)

	use 'wbthomason/packer.nvim'

	use{
		'mg979/vim-visual-multi',
		branch = 'master'
	}

	-- adds `viwS}` type things to (un)surround things with braces etc.
	use({
		'kylechui/nvim-surround',
		tag = '*',
		config = function()
			require('nvim-surround').setup()
		end
	})

	-- adds `gc[motion]` to comment/uncomment code
	use 'tpope/vim-commentary'
	-- highlights characters that can be used with fFtT
	use 'unblevable/quick-scope'
	-- adds `s[char][char]` to move to instances of "[char][char]"
	use 'justinmk/vim-sneak'
	-- Subword navigation with <leader>w etc.
	use 'bkad/CamelCaseMotion'

	vim.cmd([[
		let g:camelcasemotion_key = '<leader>'
	]])

	use 'easymotion/vim-easymotion'

	if packer_boostrap then
		require('packer').sync()
	end
end)
