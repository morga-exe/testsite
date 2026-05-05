const odbc = require('odbc');
odbc.connect('DSN=MyLibreOfficeBaseDSN;UID=;PWD=', (err, conn) => {
  if (err) throw err;
  conn.query('SELECT * FROM mytable', (err, rows) => {
    if (err) throw err;
    console.log(rows);
  });
});