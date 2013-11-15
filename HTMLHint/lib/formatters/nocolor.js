require('colors');
var util = require('util');

module.exports = {
    format: function (results, filename) {
        var output = [];
        output.push(filename + ':\n');
        results.forEach(function (result) {
            output.push(util.format('\tline %d, col %d: %s\n', result.line, result.col, result.message));
        });
        output.push('\n');
        return output.join('');
    },
    end: function (allHintCount) {
        if(allHintCount > 0){
            return util.format('%d problems.', allHintCount);
        }else{
            return util.format('No problem.');
        }
    }
};
