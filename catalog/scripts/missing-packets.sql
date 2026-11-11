-- Read-only. Missing-packet rows recorded on THIS side for one vessel (receiver view).
-- Source: RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/004_PR_REP_MISSING_PACKETS_OPERATIONS.sql
DECLARE @VESSEL_OBJECT_ID BIGINT = :vessel_object_id;

SELECT  MP.PACKET_CTR, MP.STATUS, MP.MISSING_AT, ISNULL(MP.COMM_TYPE,0) AS COMM_TYPE,
        MP.CHANNEL_ID, MP.RECD_DATE, MP.RESENT_DATE, MP.MODIFIED_ON
FROM    REP.PR_REP_Missing_Packets MP WITH (NOLOCK)
WHERE   MP.VESSEL_OBJECT_ID = @VESSEL_OBJECT_ID
  AND   MP.STATUS IN ('MSG','ERR','RCD')
ORDER BY MP.PACKET_CTR;
