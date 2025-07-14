# frozen_string_literal: true

source "https://rubygems.org"
gemspec

gem "jekyll", ENV["JEKYLL_VERSION"] if ENV["JEKYLL_VERSION"]
gem "kramdown-parser-gfm" if ENV["JEKYLL_VERSION"] == "~> 3.9"

group :jekyll_plugins do
  gem "jekyll-sitemap"
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "minima"
  gem "webrick"
end

#gem "gem", "~> 0.0.1.alpha"
gem "wdm", "~> 0.2.0"
gem 'jekyll-relative-links'