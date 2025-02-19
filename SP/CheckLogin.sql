USE [pubs_Delshad]
GO
/****** Object:  StoredProcedure [dbo].[CheckLogin]    Script Date: 6/16/2024 12:21:28 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
ALTER PROCEDURE [dbo].[CheckLogin]
	-- Add the parameters for the stored procedure here
	@UserName varchar(50),
	@Password varchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 
		UserName,
		[Password],
		FirstName,
		LastName,
		IsAdmin
	from pubs_Delshad.dbo.Users
	where UserName = @UserName  and [Password] = @Password
END
