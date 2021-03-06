const path = require('path');

module.exports = {
    entry: {
        app: './src/index.js'
    },
    watch: true,
    devtool: 'source-map',
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        // rules: [
        //     {
        //     test: /\.js$/,
        //     exclude: /node_modules/,
        //     use: ['babel-loader']
        // }]


        // the below fixed this error:
        // ERROR in ./src/index.js
        // Module build failed (from ./node_modules/babel-loader/lib/index.js):
        // SyntaxError: C:\Users\asd\Desktop\tests\CS50Web\mygithub\aditional\8-django-babel-webpack-react-Mx3ChaYA0Gw\blog\static\src\index.js: Support for the experimental syntax 'jsx' isn't currently enabled (10:5):
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/react']
                  }
                        }
        ]
    },
    resolve: {
        extensions:[
            '.js'
        ]
        }
}