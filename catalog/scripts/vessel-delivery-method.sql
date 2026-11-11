-- Read-only. Shows the delivery method (transfer type) RepTransfer will use for one vessel.
-- Source of the logic: RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L94-L125
-- If Common.CO_Parameters IS_PRODUCT = 'N', run this against the [PAL_REP] database.
DECLARE @VESSEL_OBJECT_ID BIGINT = :vessel_object_id;

SELECT  VESSEL_OBJECT_ID,
        DELIVERY_METHOD AS TRANSFER_TYPE
FROM    [REP].[REP_VESSEL_INFRA] WITH (NOLOCK)
WHERE   VESSEL_OBJECT_ID = @VESSEL_OBJECT_ID;
