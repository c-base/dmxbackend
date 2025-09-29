var path = require('path');
var webpack = require('webpack');
var FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin');


module.exports = {
  // Multiple entrypoints: https://webpack.github.io/docs/multiple-entry-points.html
  entry: {
    dmx_frontend: './src/dmx_frontend.js',
  },
  output: {
    path: path.resolve(__dirname, 'dist/'),
    publicPath: '/dist/js/',
    filename: 'js/[name].js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    }
  },
//  devServer: {
//    historyApiFallback: true,
//    noInfo: true
//  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map',
  plugins: [
    new FriendlyErrorsPlugin(),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jquery: 'jquery',
      'window.jQuery': 'jquery',
      jQuery: 'jquery'
    }),
  //    new BundleTracker({filename: 'webpack-stats.json'}),
  ]
};

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map';
  // http://vue-loader.vuejs.org/en/workflow/production.html

  module.exports.output ={
    path: path.resolve(__dirname, 'release/js/'),
    publicPath: '/dist/js/',
    filename: '[name].js'
  };
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.ProvidePlugin({
      $: 'jquery',
      jquery: 'jquery',
      'window.jQuery': 'jquery',
      jQuery: 'jquery'
    }),
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}
