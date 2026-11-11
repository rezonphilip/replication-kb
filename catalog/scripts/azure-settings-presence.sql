-- Read-only. Reports whether SmartSync storage/bus parameters are present and non-empty.
-- NEVER returns the values themselves.
SELECT  k.NAME,
        CASE WHEN p.NAME IS NULL THEN 'MISSING'
             WHEN LTRIM(RTRIM(ISNULL(p.[VALUE], ''))) = '' THEN 'EMPTY'
             ELSE 'PRESENT' END AS STATE
FROM   (VALUES ('REP_AZURE_STORAGE_ACCOUNT_NAME'),
               ('REP_AZURE_STORAGE_ACCOUNT_KEY'),
               ('REP_STORAGE_CONTAINER_NAME'),
               ('REP_CLIENT_CODE'),
               ('REP_CLIENT_ENVIROMENT_UNICID'),
               ('REP_LOCATION')) AS k(NAME)
LEFT JOIN COMMON.CO_PARAMETERS p WITH (NOLOCK) ON p.NAME = k.NAME;

-- Secret values are read by REP_GET_AZURE_SETTINGS / REP_GET_SBUS_SETTINGS from REP.REP_SERVICEBUS_CREDENTIALS,
-- not from CO_Parameters (RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/009_SP_[REP].[REP_GET_AZURE_SETTINGS].sql,
-- 010_SP_[REP].[REP_GET_SBUS_SETTINGS].sql). Presence only:
SELECT  k.NAME, 'REP_SERVICEBUS_CREDENTIALS' AS SOURCE_TABLE,
        CASE WHEN c.NAME IS NULL THEN 'MISSING'
             WHEN LTRIM(RTRIM(ISNULL(c.[VALUE], ''))) = '' THEN 'EMPTY'
             ELSE 'PRESENT' END AS STATE
FROM   (VALUES ('REP_AZURE_STORAGE_ACCOUNT_KEY')) AS k(NAME)
LEFT JOIN REP.REP_SERVICEBUS_CREDENTIALS c WITH (NOLOCK) ON c.NAME = k.NAME;
