# frozen_string_literal: true

# RubyInstaller 3.3 may fail to enumerate Jekyll's internal files when gems
# live below a hidden directory. Preload the filter modules needed while
# requiring Jekyll, then reproduce Jekyll's normal sorted directory loading.
module Jekyll
  module Filters
  end
end

require "jekyll/filters/url_filters"
require "jekyll/filters/grouping_filters"
require "jekyll/filters/date_filters"
require "jekyll"

jekyll_root = Gem::Specification.find_by_name("jekyll").gem_dir
liquid_root = Gem::Specification.find_by_name("liquid").gem_dir
liquid_tags = File.join(liquid_root, "lib/liquid/tags")
Dir.children(liquid_tags).grep(/\.rb\z/).sort.each { |file| require File.join(liquid_tags, file) }

bibtex_root = Gem::Specification.find_by_name("bibtex-ruby").gem_dir
bibtex_filters = File.join(bibtex_root, "lib/bibtex/filters")
require "bibtex/filters"
Dir.children(bibtex_filters).grep(/\.rb\z/).sort.each { |file| require File.join(bibtex_filters, file) }

%w[converters converters/markdown drops generators tags commands].each do |directory|
  path = File.join(jekyll_root, "lib/jekyll", directory)
  next unless Dir.exist?(path)

  Dir.children(path).grep(/\.rb\z/).sort.each { |file| require File.join(path, file) }
end

load File.join(jekyll_root, "exe/jekyll")
