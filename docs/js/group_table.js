function makeHeaders(columns) {
    const columnNames = {'position': 'Position', 'name': 'Name', 'played': 'Played', 'won': 'Won', 'guestWins': 'Guest Wins', 'headToHead': 'Head To Head', 'strikes': 'Strikes', 'tieBreak': 'Tie-Break'};
    var headers = $('<tr>');
    columns.forEach(column => {
        headers.append($('<th>').text(columnNames[column]));
    });
    return headers;
}

function hashEntry(columns, entry) {
    var hashFields = [];
    for (column of columns) {
        if (column == 'headToHead' && entry[column]) {
            var winList = entry[column].split(',').map(function(score) {
                return Number(score.split('-')[0]);
            });
            hashFields.push(winList);
        } else if (!['position', 'name', 'played'].includes(column)) {
            hashFields.push(entry[column]);
        }
    }
    return hashFields.join('|');
}

function makePlayerLink(id, players) {
    return $('<a>').attr('href', 'player.html?player=' + id).text(players[id]['name']);
}

function compareEntriesFn(columnOrder) {
    debug('columnOrder', columnOrder);
    return function(entryA, entryB) {
        debug('entryA', entryA);
        debug('entryB', entryB);
        if (('seasonForfeit' in entryA) != ('seasonForfeit' in entryB)) {
            return entryA['seasonForfeit'];
        }
        for (const columnInfo of columnOrder) {
            const column = Object.keys(columnInfo)[0];
            const direction = columnInfo[column] == 'ASC';
            var valueA = (column in entryA && entryA[column]) ? '' + entryA[column] : '0';
            var valueB = (column in entryB && entryB[column]) ? '' + entryB[column] : '0';
            if (column == 'headToHead' || column == 'tieBreak') {
                valueA = valueA.split(', ').map(score => score.split('-')[0]);
                valueB = valueB.split(', ').map(score => score.split('-')[0]);
                for (var i = 0; i < valueA.length; i++) {
                    if (valueA[i] == valueB[i]) {
                        continue;
                    }
                    return ((valueA[i] > valueB[i]) == direction);
                }
            } else {
                valueA = Number(valueA);
                valueB = Number(valueB);
                if (valueA == valueB) {
                    continue;
                }
                debug('valueA', valueA);
                debug('valueB', valueB);
                debug('result', ((valueA > valueB) == direction));
                return ((valueA > valueB) == direction);
            }
        }
        debug('Dropped out', true);
    }
}

function makeRows(columnOrder, entries, players) {
    var columns = ['position', 'name', 'played'];
    columnOrder.forEach(column => columns.push(Object.keys(column)[0]));
    var tbody = $('<tbody>');
    var positionCounter = {};
    for (entry of entries) {
        var key = hashEntry(columns, entry);
        if (!Object.keys(positionCounter).includes(key)) {
            positionCounter[key] = 0;
        }
        positionCounter[key]++;
    }
    var currentPosition = 1;
    var countAtPosition = 0;

    debug('entriesBeforeSort', entries);

    entries.sort(compareEntriesFn(columnOrder));

    debug('entriesAfterSort', entries);

    entries.forEach(function(entry, i) {
        var row = $('<tr>');
        columns.forEach(column => {
            var text = entry[column];
            if (column == 'position') {
                var totalAtPosition = positionCounter[hashEntry(columns, entry)];
                if (totalAtPosition > 1) {
                    text = '=' + currentPosition;
                } else {
                    text = currentPosition;
                }
                countAtPosition++;
                if (countAtPosition == totalAtPosition) {
                    currentPosition += countAtPosition;
                    countAtPosition = 0;
                }

                if (entry['seasonForfeit']) {
                    text = 'SF';
                }
            }
            var cell = $('<td>');
            if (column == 'name') {
                cell.append(makePlayerLink(entry['id'], players));
            } else {
                cell.text(text);
            }
            row.append(cell);
        });
        tbody.append(row);
    });
    return tbody;
}

function makePlayoff(playoff, players) {
    var table = $('<table>').attr('id', 'results');
    var tbody = $('<tbody>');
    table.append(tbody);
    for (result of playoff) {
        var row = $('<tr>');
        var sortedPlayerIds = Object.keys(result).sort(function(playerA, playerB) { return result[playerB] - result[playerA]; });
        row.append($('<td>').append(makePlayerLink(sortedPlayerIds[0], players)));
        var resultText = result[sortedPlayerIds[0]] + ' - ' + result[sortedPlayerIds[1]];
        if (Object.keys(result).includes('awards')) {
            resultText = result['awards'][0] + ' ' + resultText + ' ' + result['awards'][1];
        }
        row.append($('<td>').text(resultText));
        row.append($('<td>').append(makePlayerLink(sortedPlayerIds[1], players)));
        tbody.append(row);
    }
    return table;
}
