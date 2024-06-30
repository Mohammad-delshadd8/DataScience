-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AddEmployee] 
	-- Add the parameters for the stored procedure here
	@EmployeeID varchar(10),
	@EmployeeFirstName  varchar(50),
	@EmployeeLastName  varchar(50),
	@EmployeeJobID smallint,
	@EmployeePublisherID varchar(5),
	@EmployeeHireDate datetime

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	insert pubs_Delshad.dbo.employee(emp_id,fname,lname,job_id,pub_id,hire_date)
	values(@EmployeeID, @EmployeeFirstName, @EmployeeLastName, @EmployeeJobID, @EmployeePublisherID, @EmployeeHireDate)

END
GO
