-- Read-only. Reports whether Service Bus / integration parameters are present and non-empty.
-- NEVER returns the values themselves.
SELECT  k.NAME,
        CASE WHEN p.NAME IS NULL THEN 'MISSING'
             WHEN LTRIM(RTRIM(ISNULL(p.[VALUE], ''))) = '' THEN 'EMPTY'
             ELSE 'PRESENT' END AS STATE
FROM   (VALUES ('REP_SERVICEBUS_CONNECTION_STRING'),
               ('REP_INTERGRATION_BASE_URL'),
               ('REP_INTERGRATION_API_URL'),
               ('REP_LOCATION')) AS k(NAME)
LEFT JOIN COMMON.CO_PARAMETERS p WITH (NOLOCK) ON p.NAME = k.NAME;
-- Queue names come from REP.REP_PR_SUBSCRIBER_LIST (read by REP.REP_GET_QUEUE_NAME,
-- RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/044_[REP].[REP_GET_QUEUE_NAME].sql#L6-L16).
-- Count only (queue names are not shown):
SELECT  [TYPE], COUNT(*) AS SUBSCRIBERS,
        SUM(CASE WHEN LTRIM(RTRIM(ISNULL(QUEUE_NAME,''))) = '' THEN 1 ELSE 0 END) AS EMPTY_QUEUE_NAMES
FROM    REP.REP_PR_SUBSCRIBER_LIST WITH (NOLOCK)
GROUP BY [TYPE];

-- Secret values are read by REP_GET_AZURE_SETTINGS / REP_GET_SBUS_SETTINGS from REP.REP_SERVICEBUS_CREDENTIALS,
-- not from CO_Parameters (RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/009_SP_[REP].[REP_GET_AZURE_SETTINGS].sql,
-- 010_SP_[REP].[REP_GET_SBUS_SETTINGS].sql). Presence only:
SELECT  k.NAME, 'REP_SERVICEBUS_CREDENTIALS' AS SOURCE_TABLE,
        CASE WHEN c.NAME IS NULL THEN 'MISSING'
             WHEN LTRIM(RTRIM(ISNULL(c.[VALUE], ''))) = '' THEN 'EMPTY'
             ELSE 'PRESENT' END AS STATE
FROM   (VALUES ('REP_SERVICEBUS_CONNECTION_STRING')) AS k(NAME)
LEFT JOIN REP.REP_SERVICEBUS_CREDENTIALS c WITH (NOLOCK) ON c.NAME = k.NAME;
