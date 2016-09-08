function parseCommandLineArguments(commandLineArguments) {
  var parseArgs = require('minimist');
  var parsedCommandLineArguments = parseArgs(commandLineArguments, commandLineParserOptions());
  return {
    port: parsedCommandLineArguments.port,
  };
}

function commandLineParserOptions() {
  var buildOptions = require('minimist-options');
  var options = {
    port: {
      alias: 'p',
      default: defaultPort()
    }
  };
  return buildOptions(options);
}

function defaultPort() {
  return 5000;
}

module.exports = parseCommandLineArguments;
